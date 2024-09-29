from rest_framework import serializers
from account.models import User
from product.models import Product, Size, Color
from .models import Cart, CartItem, Order, OrderItem


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('title',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('title',)


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='title', queryset=Product.objects.all())
    size = SizeSerializer(many=True)
    color = ColorSerializer(many=True)

    class Meta:
        model = CartItem
        exclude = ('cart',)


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Cart
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='title', queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        exclude = ('order',)


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
