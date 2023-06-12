"""
Contains a function tthat updates the features of a vehicle.
"""
from ..models import VehicleFeature
from ..functions.create_vehicle_features import create_vehicle_features


def update_vehicle_features(feature_list: list, vehicle):
    """
    - Takes a vehicle object.
    - Takes a list of features in this format:

    [

        [<Feature Name>,<Feature Description>],

        [<Feature Name>,<Feature Description>],

        [<Feature Name>,<Feature Description>],

        [<Feature Name>,<Feature Description>],

    ]

    """
    vehicle_features = VehicleFeature.objects.filter(vehicle=vehicle)

    if len(vehicle_features) > 0:
        for feature in vehicle_features:
            feature.delete()

    if feature_list is not None:
        if isinstance(feature_list, list) is True:
            status = create_vehicle_features(
                features=feature_list, vehicle=vehicle)

            return status
