from rest_framework import serializers
from inflows.models import Inflows


class InflowSerializer(serializers.ModelSerializer):

    class Meta:
        models = Inflows
        fields = '__all__'
