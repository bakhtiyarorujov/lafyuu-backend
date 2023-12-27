from rest_framework import generics, permissions
from rest_framework import parsers
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CategorySerializer,
    CommentCreateSerializer,
    CommentListSerialzier)
from .models import (
    Product,
    ProductVersion,
    Category,
    ProductsComment
)
# Create your views here.

class ProductListView(generics.ListAPIView):
    '''List products filtered by category ID'''
    queryset = ProductVersion.objects.filter(display = True)
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id = category_id)
        queryset = ProductVersion.objects.filter(display = True, product__category = category)
        return queryset


class ProductMegaListView(generics.ListAPIView):
    '''Get mega sale products'''
    queryset = ProductVersion.objects.filter(display = True).order_by('-discount__discount')
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]


class ProductFlashListView(generics.ListAPIView):
    '''Get flash sale products'''
    queryset = ProductVersion.objects.filter(display = True).order_by('-stock')
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]


class ProductRecomListView(generics.ListAPIView):
    '''Get recommended products'''
    queryset = ProductVersion.objects.filter(display = True).order_by('stock')
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]


class ProductCategories(generics.ListAPIView):
    '''Get all available categories'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductDetailView(generics.RetrieveAPIView):
    '''Get product details'''
    queryset = ProductVersion.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        product_id = self.kwargs.get('product_id')
        product = ProductVersion.objects.get(id = product_id)
        return product
    
class CommentCreateView(generics.CreateAPIView):
    '''Create comment. Please use parent_id to create a comment'''
    queryset = ProductsComment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

class CommentListView(generics.ListAPIView):
    '''List comment by Product ID'''
    queryset = ProductsComment.objects.all()
    serializer_class = CommentListSerialzier

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(version__id = product_id)
        queryset = ProductsComment.objects.filter(product = product)
        return queryset