from rest_framework import serializers
from .models import MenuItem, Category, Order, OrderItem
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        category = CategorySerializer
        fields = ['id', 'title', 'price', 'category', 'featured']
        extra_kwargs = {
            'price': {'min_value': 2},
        }

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        user = User
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date']

class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    class Meta:
        order = User
        menuitem = MenuItem
        model = OrderItem
        fields = ['id', 'order', 'menuitem', 'quantity', 'unit_price', 'price']
        read_only_fields = ['price']

    def get_price(self, data):
        return data.quantity * data.unit_price