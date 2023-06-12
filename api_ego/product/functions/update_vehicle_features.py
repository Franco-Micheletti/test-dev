"""
Contains a function tthat updates the features of a vehicle.
"""
from ..models import VehicleFeature, FeatureDescription


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

    if feature_list is not None:
        if isinstance(feature_list, list) is True:
            for feature_couple in feature_list:
                feature_name_to_update = feature_couple[0]
                new_description = feature_couple[1]

                vehicle_feature = VehicleFeature.objects.get(
                    vehicle=vehicle, feature__feature_name__name=feature_name_to_update)

                if vehicle_feature:
                    description_object = FeatureDescription.objects.get(
                        description=vehicle_feature.feature.feature_description.description)

                    if description_object:
                        description_object.description = new_description
                        description_object.save()
