from rest_framework import serializers
from account.models import User
from .models import Product, ProductReview, Color, Category, Size, Comment


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all(), many=True)
    size = serializers.SlugRelatedField(slug_field='title', queryset=Size.objects.all(), many=True)
    color = serializers.SlugRelatedField(slug_field='title', queryset=Color.objects.all(), many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('title',)


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    product = serializers.SlugRelatedField(slug_field='title', queryset=Product.objects.all())
    parent = serializers.SlugRelatedField(slug_field='text', queryset=Comment.objects.all(), allow_null=True,
                                          required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='title', queryset=Product.objects.all())
    user = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = ProductReview
        fields = '__all__'
