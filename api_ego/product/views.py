"""
Product views
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_200_OK,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
from .models import Vehicle
from .serializers import VehicleSerializer

# Functions
from .functions.update_vehicle_features import update_vehicle_features
from .functions.get_features_of_vehicle import get_features_of_vehicle
from .functions.create_vehicle_features import create_vehicle_features


class SpecificVehicle(APIView):
    """
    Endpoint that will allow to modified one vehicle add a new one or delete an existing one
    Methods allow are the following : GET , PUT , DELETE
    """

    def get(self, request, vehicle_id):
        """
        Returns vehicle specific data
        """
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
        except Vehicle.DoesNotExist:
            return Response("Vehicle does not exist")

        vehicle_basic_data = VehicleSerializer(vehicle).data

        # Get features of the vehicle
        vehicle_features_data = get_features_of_vehicle(vehicle=vehicle)

        response_data = {"basic": vehicle_basic_data,
                         "features": vehicle_features_data}

        return Response(response_data, status=HTTP_200_OK)

    def delete(self, request, vehicle_id):
        """
        Deletes specific vehicle
        """
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
        except Vehicle.DoesNotExist:
            return Response("Vehicle does not exist", status=HTTP_404_NOT_FOUND)

        try:
            if vehicle:
                vehicle_deleted = vehicle.delete()
                if vehicle_deleted[0] > 0:
                    return Response("Vehicle deleted successfully")
                return Response("Error while deleting the resource")
        except Exception as error:
            message = "Can't delete resource\n" + "ERROR: " + error
            return Response(message, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, vehicle_id):
        """
        Updates data of the vehicle with the data provided , 
        if a field is missing in the request body, the current data of the vehicle will be used
        """
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
        except Vehicle.DoesNotExist:
            return Response("Vehicle does not exist")

        vehicle.name = request.data.get('name', vehicle.name)
        vehicle.type = request.data.get('type', vehicle.type)
        vehicle.model = request.data.get('model', vehicle.model)
        vehicle.brand = request.data.get('brand', vehicle.brand)
        vehicle.price = request.data.get('price', vehicle.price)
        vehicle.date = request.data.get('date', vehicle.date)

        vehicle.save()
        # Update vehicle features if any
        features = request.data.get('features', None)
        update_vehicle_features(feature_list=features, vehicle=vehicle)

        response_data = {"message": "Vehicle updated successfully",
                         "vehicle_data": VehicleSerializer(vehicle).data}

        return Response(response_data, status=HTTP_200_OK)


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

        # Create vehicle features
        feature_list = request.data.get('features', None)
        if feature_list is not None:
            if isinstance(feature_list, list) is True:
                status = create_vehicle_features(
                    features=feature_list, vehicle=new_vehicle)
                if status != 1:
                    return Response(status, HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response("Vehicle features must be a list", status=HTTP_400_BAD_REQUEST)

        return Response({"message": "Vehicle Created successfully",
                         "vehicle_basic": new_vehicle_data}, status=HTTP_201_CREATED)
