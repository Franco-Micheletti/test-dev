"""
Contains a function that fetch the vehicles images from the database
"""
from ..models import VehicleImage
from ..serializers import VehicleImageSerializer


def get_vehicle_images(vehicle):
    """
    - Takes a vehicle object

    Return all the images data for the specific vehicle.
    """
    try:
        vehicle_images = VehicleImage.objects.filter(vehicle=vehicle)
    except VehicleImage.DoesNotExist:
        return "not found"

    vehicle_images_data = VehicleImageSerializer(
        vehicle_images, many=True).data

    return vehicle_images_data
