from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from product.pagination import StandardResultSetPagination
from .permissions import ReadOnlyUser, ProductUpdater, ProductDeleter, ProductCreater
from .serializers import ProductSerializer, CategorySerializer, ColorSerializer, SizeSerializer, CommentSerializer, \
    ProductReviewSerializer
from .models import Product, Category, Color, Comment, Size, ProductReview
from .permissions import CategoryCreater, CategoryDeleter, CategoryUpdater
from .permissions import ColorCreater, ColorDeleter, ColorUpdater
from .permissions import SizeCreater, SizeDeleter, SizeUpdater


class ProductListView(APIView, StandardResultSetPagination):
    permission_classes = [ReadOnlyUser]

    def get(self, request):
        products = Product.objects.all()
        result = self.paginate_queryset(products, request)
        serializer = ProductSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class ProductDetailView(APIView):
    permission_classes = [ReadOnlyUser]

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductUpdateView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, ProductUpdater]

    def put(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCreateView(APIView):
    permission_classes = [IsAdminUser, ProductCreater, IsAuthenticated]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(APIView):
    permission_classes = [IsAdminUser, ProductDeleter, IsAuthenticated]

    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return Response({'response': 'product removed'})


# ------------------------------------------------------------------------------------

class CategoryListView(APIView, StandardResultSetPagination):
    permission_classes = [ReadOnlyUser]

    def get(self, request):
        categories = Category.objects.all()
        result = self.paginate_queryset(categories, request)
        serializer = CategorySerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class CategoryDetailView(APIView):
    permission_classes = [ReadOnlyUser]

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(instance=category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryUpdateView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, CategoryUpdater]

    def put(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, CategoryDeleter]

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()
        return Response({'response': 'category removed'})


class CategoryCreateView(APIView):
    permission_classes = [IsAdminUser, CategoryCreater, IsAuthenticated]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------

class ColorListView(APIView, StandardResultSetPagination):
    permission_classes = [ReadOnlyUser]

    def get(self, request):
        colors = Color.objects.all()
        result = self.paginate_queryset(colors, request)
        serializer = ColorSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class ColorDetailView(APIView):
    permission_classes = [ReadOnlyUser]

    def get(self, request, pk):
        color = get_object_or_404(Color, id=pk)
        serializer = ColorSerializer(instance=color)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ColorUpdateView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, ColorUpdater]

    def put(self, request, pk):
        color = get_object_or_404(Color, id=pk)
        serializer = ColorSerializer(instance=color, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorDeleteView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, ColorDeleter]

    def delete(self, request, pk):
        color = get_object_or_404(Color, id=pk)
        color.delete()
        return Response({'response': 'color removed'})


class ColorCreateView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, ColorCreater]

    def post(self, request):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------

class SizeListView(APIView, StandardResultSetPagination):
    permission_classes = [ReadOnlyUser]

    def get(self, request):
        sizes = Size.objects.all()
        result = self.paginate_queryset(sizes, request)
        serializer = SizeSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class SizeDetailView(APIView):
    permission_classes = [ReadOnlyUser]

    def get(self, request, pk):
        size = get_object_or_404(Size, id=pk)
        serializer = SizeSerializer(instance=size)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SizeUpdateView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, SizeUpdater]

    def put(self, request, pk):
        size = get_object_or_404(Size, id=pk)
        serializer = SizeSerializer(instance=size, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SizeDeleteView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, SizeDeleter]

    def delete(self, request, pk):
        size = get_object_or_404(Size, id=pk)
        size.delete()
        return Response({'response': 'size removed'})


class SizeCreateView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated, SizeCreater]

    def post(self, request):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------

class CommentListView(APIView, StandardResultSetPagination):
    permission_classes = [ReadOnlyUser]

    def get(self, request):
        comments = Comment.objects.all()
        result = self.paginate_queryset(comments, request)
        serializer = CommentSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class CommentDetailView(APIView):
    permission_classes = [ReadOnlyUser]

    def get(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        serializer = CommentSerializer(instance=comment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        comment.delete()
        return Response({'response': 'comment removed'})


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------
class ProductReviewListView(APIView, StandardResultSetPagination):
    permission_classes = [ReadOnlyUser]

    def get(self, request):
        reviews = ProductReview.objects.all()
        result = self.paginate_queryset(reviews, request)
        serializer = ProductReviewSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)


class ProductReviewDetailView(APIView):
    permission_classes = [ReadOnlyUser]

    def get(self, request, pk):
        review = get_object_or_404(ProductReview, id=pk)
        serializer = ProductReviewSerializer(instance=review)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductReviewCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductReviewDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        review = get_object_or_404(Product, id=pk)
        review.delete()
        return Response({'response': 'review removed'})
