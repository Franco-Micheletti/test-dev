"""
Contains a function to get all the features of a vehicle object.
"""
from ..models import VehicleFeature


def get_features_of_vehicle(vehicle):
    """
    Takes a vehicle object and returns all of its features
    """
    vehicle_features_data = {}
    features_objects = VehicleFeature.objects.filter(vehicle=vehicle)
    for obj in features_objects:
        name = obj.feature.feature_name.name
        description = obj.feature.feature_description.description
        vehicle_features_data[name] = description

    return vehicle_features_data
