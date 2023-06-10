"""
Product serializers
"""
from rest_framework.serializers import ModelSerializer
from .models import Vehicle


class VehicleSerializer(ModelSerializer):
    """
    Vehicle Serializer
    """
    class Meta:
        model = Vehicle
        fields = ('id',
                  'name',
                  'type',
                  'model',
                  'brand',
                  'price',
                  'date',
                  )
