"""
Product views
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import Vehicle, FeatureName, FeatureDescription, FeatureCouple, VehicleFeature
from .serializers import VehicleSerializer


class SpecificVehicle(APIView):
    """
    Endpoint that will allow to modified one vehicle add a new one or delete an existing one
    Methods allow are the following : GET , PUT , DELETE
    """


class CreateVehicle(APIView):
    """
    Endpoint that will allow to create a new vehicle with the data provided in the request body
    """

    def post(self, request):
        """
        Post method for creating a vehicle
        """
        # Create vehicle basic info
        new_vehicle = Vehicle.objects.create(
            name=request.data.get('name'),
            type=request.data.get('type', None),
            model=request.data.get('model', None),
            brand=request.data.get('brand', None),
            price=request.data.get('price', None),
            date=request.data.get('date', None)
        )
        if new_vehicle:
            new_vehicle_data = VehicleSerializer(new_vehicle).data

        # Create or get vehicle features
        features = request.data.get('features', None)
        if features is not None:
            if isinstance(features, list) is True:
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
                        vehicle=new_vehicle, feature=feature_couple[0])

            else:
                return Response("Vehicle features must be a list", status=HTTP_400_BAD_REQUEST)

        return Response({"message": "Vehicle Created successfully",
                         "vehicle": new_vehicle_data}, status=HTTP_201_CREATED)
