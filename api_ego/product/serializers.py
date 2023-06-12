"""
Product serializers
"""
from rest_framework.serializers import ModelSerializer
from .models import Vehicle, VehicleImage


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
                  'date'
                  )


class VehicleImageSerializer(ModelSerializer):
    """
    Vehicle image serializer
    """
    class Meta:
        model = VehicleImage
        fields = ('url',
                  'title',
                  'detail')
