from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('list', views.ProductListView.as_view(), name='product-list'),
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('update/<int:pk>', views.ProductUpdateView.as_view(), name='product-update'),
    path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product-delete'),
    path('create', views.ProductCreateView.as_view(), name='product-create'),

    path('category/list', views.CategoryListView.as_view(), name='category-list'),
    path('category/detail/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/update/<int:pk>', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('category/create', views.CategoryCreateView.as_view(), name='category-create'),

    path('color/list', views.ColorListView.as_view(), name='color-list'),
    path('color/detail/<int:pk>', views.ColorDetailView.as_view(), name='color-detail'),
    path('color/update/<int:pk>', views.ColorUpdateView.as_view(), name='color-update'),
    path('color/delete/<int:pk>', views.ColorDeleteView.as_view(), name='color-delete'),
    path('color/create', views.ColorCreateView.as_view(), name='color-create'),

    path('size/list', views.SizeListView.as_view(), name='size-list'),
    path('size/detail/<int:pk>', views.SizeDetailView.as_view(), name='size-detail'),
    path('size/update/<int:pk>', views.SizeUpdateView.as_view(), name='size-update'),
    path('size/delete/<int:pk>', views.SizeDeleteView.as_view(), name='size-delete'),
    path('size/create', views.SizeCreateView.as_view(), name='size-create'),

    path('comment/list', views.CommentListView.as_view(), name='comment-list'),
    path('comment/detail/<int:pk>', views.CommentDetailView.as_view(), name='comment-detail'),
    path('comment/delete/<int:pk>', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/create', views.CommentCreateView.as_view(), name='comment-create'),

    path('review/list', views.ProductReviewListView.as_view(), name='review-list'),
    path('review/detail/<int:pk>', views.ProductReviewDetailView.as_view(), name='review-detail'),
    path('review/delete/<int:pk>', views.ProductReviewDeleteView.as_view(), name='review-delete'),
    path('review/create', views.ProductReviewCreateView.as_view(), name='review-create')

]



