from main_app.models import Product, ProductVersion, ProductAndCount, Cart, Order
from django.contrib.auth.models import User
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class ProductVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion
        exclude = ()


class ProductAndCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAndCount
        exclude = ()


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
