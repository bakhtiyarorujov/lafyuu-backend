from django.contrib import admin
from .models import (
    Product,
    ProductVersion,
    ProductImages,
    ProductsComment,
    Commentimages,
    Brand,
    Category,
    Discount,
    Color,
    Size
)

# Register your models here.

class ProductVersionInlineAdmin(admin.TabularInline):
    model = ProductVersion


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_brand', 'get_category']
    inlines = [ProductVersionInlineAdmin]

    def get_brand(self, obj):
        return obj.brand.name
    
    def get_category(self, obj):
        return obj.category.name
    
    get_brand.short_description = "Brand"
    get_category.short_description = "Category"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount']


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'color', 'size', 'stock', 'price', 'discount', 'display']
    list_display_links = ['get_name', 'color', 'size', 'stock', 'price', 'discount']
    inlines = [ProductImagesAdmin]

    def get_name(self, obj):
        return obj.product.name
    
    get_name.short_description = 'Name'


@admin.register(ProductImages)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'product']


class CommentImagesAdmin(admin.TabularInline):
    model = Commentimages

@admin.register(ProductsComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating']
    inlines = (CommentImagesAdmin,)