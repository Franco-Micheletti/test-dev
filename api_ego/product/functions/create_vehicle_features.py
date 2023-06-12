"""
Contains a function that creates the features of 
one vehicle object with the data provided
"""
from ..models import FeatureName, FeatureDescription, FeatureCouple, VehicleFeature


def create_vehicle_features(features, vehicle):
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

    # Reusable objects prevent duplicate data in case two vehicles have
    # the same feature_name or the same description
    # if the function does not found any object with the same value it creates a new one

    try:
        for feature_couple in features:
            feature_name = feature_couple[0]
            feature_description = feature_couple[1]

            name_object = FeatureName.objects.get_or_create(
                name=feature_name,
            )
            description_object = FeatureDescription.objects.get_or_create(
                description=feature_description
            )

            feature_couple = FeatureCouple.objects.get_or_create(
                feature_name=name_object[0],
                feature_description=description_object[0]
            )

            # Add features to vehicle

            VehicleFeature.objects.create(
                vehicle=vehicle, feature=feature_couple[0])

        return 1
    except Exception as error:
        return error
