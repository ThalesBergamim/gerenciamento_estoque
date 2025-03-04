from rest_framework import serializers
from outflow.models import Outflow


class OutflowSerializer(serializers.ModelSerializer):

    class Meta:
        models = Outflow
        fields = '__all__'
