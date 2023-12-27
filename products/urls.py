from django.urls import path
from .views import (
    ProductListView,
    ProductMegaListView,
    ProductFlashListView,
    ProductRecomListView,
    ProductCategories,
    ProductDetailView,
    CommentCreateView,
    CommentListView
)

urlpatterns = [
    path('<int:category_id>', ProductListView.as_view(), name='products'),
    path('mega/', ProductMegaListView.as_view(), name='products_mega'),
    path('flash/', ProductFlashListView.as_view(), name='products_flash'),
    path('recommended/', ProductRecomListView.as_view(), name='products_recom'),
    path('detail/<int:product_id>', ProductDetailView.as_view(), name='product_detail'),
    path('categories/', ProductCategories.as_view(), name='products_cat'),
    path('comment/', CommentCreateView.as_view(), name='products_comment'),
    path('comment/<int:product_id>', CommentListView.as_view(), name='products_comments'),
]