from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        models = Product
        fields = '__all__'
