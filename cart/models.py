from django.db import models
from account.models import User
from product.models import Product, Size, Color


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(default=0)
    size = models.ManyToManyField(Size, blank=True, related_name='cart_item')
    color = models.ManyToManyField(Color, blank=True, related_name='cart_item')

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    address = models.TextField(default='-')

    def __str__(self):
        return self.user.email


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    size = models.CharField(max_length=12, null=True, blank=True)
    color = models.CharField(max_length=15, null=True, blank=True)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.order.user.email
