from rest_framework import serializers
from django.db.models import Avg   
from django.contrib.auth import get_user_model 
from .models import (
    ProductVersion,
    ProductsComment,
    ProductImages,
    Commentimages,
    Category,
    Size,
    Color)

User = get_user_model()

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = (
            'id',
            'image',
        )


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            'id',
            'name'
        )


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'id',
            'name'
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source = 'product.name')
    brand = serializers.CharField(source = 'product.brand.name')
    category = serializers.CharField(source = 'product.category.name')
    description = serializers.CharField(source = 'product.description')
    parent_id = serializers.IntegerField(source = 'product.id')
    discount = serializers.IntegerField(source = 'discount.discount')
    discounted_price = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    available_sizes = serializers.SerializerMethodField()
    available_colors = serializers.SerializerMethodField()
    images = ProductImagesSerializer(many = True)
    class Meta:
        model = ProductVersion
        fields = (
            'id',
            'parent_id',
            'name',
            'brand',
            'category',
            'description',
            'stock',
            'price',
            'discount',
            'discounted_price',
            'color',
            'size',
            'rating',
            'review_count',
            'available_sizes',
            'available_colors',
            'images'
        )
    
    def get_discounted_price(self, instance):
        if instance.discount:
            new_price = instance.price * (100 - instance.discount.discount)/100
            rounded_price = round(new_price, 2)
            return rounded_price
        return instance.price

    def get_rating(self, instance):
        product_id = instance.product.id
        average_rating = ProductsComment.objects.filter(product_id=product_id).aggregate(Avg('rating'))['rating__avg']
        return average_rating
    
    def get_review_count(self, instance):
        product_id = instance.product.id
        comments_count = ProductsComment.objects.filter(product_id=product_id).count()
        return comments_count

    def get_available_sizes(self, instance):
        product = instance.product
        sizes = Size.objects.filter(product_size__product = product)
        serialized_sizes = SizeSerializer(sizes, many=True).data
        return serialized_sizes
    
    def get_available_colors(self, instance):
        product = instance.product
        colors = Color.objects.filter(product_color__product = product).distinct()
        serialized_colors = ColorSerializer(colors, many = True).data
        return serialized_colors


class ProductListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source = 'product.name')
    discount = serializers.IntegerField(source = 'discount.discount')
    discounted_price = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    class Meta:
        model = ProductVersion
        fields = (
            'id',
            'name',
            'image',
            'price',
            'discount',
            'discounted_price',
            'rating',
            'review_count'
        )

    def get_discounted_price(self, instance):
        if instance.discount:
            new_price = instance.price * (100 - instance.discount.discount)/100
            rounded_price = round(new_price, 2)
            return rounded_price
        return instance.price
    
    def get_rating(self, instance):
        product_id = instance.product.id
        average_rating = ProductsComment.objects.filter(product_id=product_id).aggregate(Avg('rating'))['rating__avg']
        return average_rating
    
    def get_review_count(self, instance):
        product_id = instance.product.id
        comments_count = ProductsComment.objects.filter(product_id=product_id).count()
        return comments_count
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'email'
        )


class CommentImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentimages
        fields = (
            'id',
            'image'
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    images= CommentImagesSerializer(read_only = True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
        required = False
    ) 
    class Meta:
        model = ProductsComment
        fields = (
            'user',
            'product',
            'rating',
            'comment',
            'images',
            'uploaded_images'
        )
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", None)
        user = self.context['request'].user
        comment = ProductsComment.objects.create(user = user, **validated_data)

        if uploaded_images is not None:
            for image in uploaded_images:
                Commentimages.objects.create(image = image, comment = comment)

        return comment


class CommentListSerialzier(serializers.ModelSerializer):
    user = UserSerializer()
    comment_images = CommentImagesSerializer(many = True)
    class Meta:
        model = ProductsComment
        fields = (
            'id',
            'user',
            'comment_images',
            'rating',
            'comment',
            'date'
        )