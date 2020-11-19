from rest_framework import serializers
from .models import Seller, Product


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'email', 'url']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'seller', 'quantity', 'status', 'url']

