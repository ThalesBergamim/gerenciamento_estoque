from rest_framework import serializers
from supplier.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        models = Supplier
        fields = '__all__'
