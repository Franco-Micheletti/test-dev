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

from .functions.get_features_of_vehicle import get_features_of_vehicle
from .functions.get_vehicle_images import get_vehicle_images

from .functions.create_vehicle_features import create_vehicle_features
from .functions.create_vehicle_images import create_vehicle_images

from .functions.update_vehicle_features import update_vehicle_features
from .functions.update_vehicle_images import update_vehicle_images


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

        response_data = {"basic": vehicle_basic_data,
                         "features": get_features_of_vehicle(vehicle=vehicle),
                         "images": get_vehicle_images(vehicle=vehicle)}

        return Response(response_data, status=HTTP_200_OK)

    def delete(self, request, vehicle_id):
        """
        Deletes specific vehicle
        """
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
        except Vehicle.DoesNotExist:
            message = "Vehicle does not exist"
            return Response(message, status=HTTP_404_NOT_FOUND)

        try:
            if vehicle:
                vehicle_deleted = vehicle.delete()
                if vehicle_deleted[0] > 0:
                    message = "Vehicle deleted successfully"
                else:
                    message = "Error while deleting the resource"
                    return Response(message, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as error:
            message = "Can't delete resource\n" + "ERROR: " + error
            return Response(message, status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(message, status=HTTP_200_OK)

    def put(self, request, vehicle_id):
        """
        Updates data of the vehicle with the data provided , 
        if a field is missing in the request body, the current data of the vehicle will be used

        **SAMPLE REQUEST BODY**
        ```
        {
            "name": "Hilux Conquest",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 19300000,
            "features":[
                            ["seguridad","7 airbags: frontales (conductor y acompañante), de rodilla (conductor), laterales (x2) y de cortina (x2)"],
                            ["confort","Audio con pantalla táctil de 8“ y Control de velocidad crucero"],
                            ["exterior","Faros delanteros halógenos con regulación en altura y Sistema 'Follow me home'"],
                            ["transmision","Manual de 6 velocidades. Traccion 4x2"]
                        ],
            "images": [
                {
                    "url": "https://test/images/fake/1.png",
                    "title": "image title 1 updated",
                    "detail": "image detail 1 updated"
                },
                {
                    "url": "https://test/images/fake/2.png",
                    "title": "image title 2 updated",
                    "detail": "image detail 2 updated"
                }
            ]
        }
        ```
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
        if features:
            status = update_vehicle_features(
                feature_list=features, vehicle=vehicle)
            if status != 1:
                return Response(status, HTTP_500_INTERNAL_SERVER_ERROR)
        # Update vehicle images if any
        images = request.data.get('images', None)
        if images:
            status = update_vehicle_images(image_list=images, vehicle=vehicle)
            if status != 1:
                if status == "missing url":
                    return Response("Image URL is required", status=HTTP_400_BAD_REQUEST)
                return Response(status, status=HTTP_500_INTERNAL_SERVER_ERROR)

        response_data = {"message": "Vehicle updated successfully",
                         "basic": VehicleSerializer(vehicle).data,
                         "features": get_features_of_vehicle(vehicle=vehicle),
                         "images": get_vehicle_images(vehicle=vehicle)}

        return Response(response_data, status=HTTP_200_OK)


class CreateVehicle(APIView):
    """
    Endpoint that will allow to create a new vehicle with the data provided in the request body
    """

    def post(self, request):
        """
        Post method for creating a vehicle

        **SAMPLE REQUEST BODY**
        ```
        {
            "name": "Hilux Conquest",
            "type": "Pickups",
            "model": "Conquest",
            "brand": "Toyota",
            "date": "2023-06-23",
            "price": 19300000,
            "features":[
                            ["seguridad","7 airbags: frontales (conductor y acompañante), de rodilla (conductor), laterales (x2) y de cortina (x2)"],
                            ["confort","Audio con pantalla táctil de 8“ y Control de velocidad crucero"],
                            ["exterior","Faros delanteros halógenos con regulación en altura y Sistema 'Follow me home'"],
                            ["transmision","Manual de 6 velocidades. Traccion 4x2"]
                        ],
            "images": [
                {
                    "url": "https://test/images/fake/1.png",
                    "title": "image title 1 updated",
                    "detail": "image detail 1 updated"
                },
                {
                    "url": "https://test/images/fake/2.png",
                    "title": "image title 2 updated",
                    "detail": "image detail 2 updated"
                }
            ]
        }
        ```
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

        # Create vehicle features if any
        feature_list = request.data.get('features', None)
        if feature_list is not None:
            if isinstance(feature_list, list) is True:
                status = create_vehicle_features(
                    features=feature_list, vehicle=new_vehicle)
                if status != 1:
                    return Response(status, HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response("Vehicle features must be a list", status=HTTP_400_BAD_REQUEST)

        # Create vehicle images if any
        images = request.data.get('images', None)
        if images is not None:
            status = create_vehicle_images(
                image_list=images, vehicle=new_vehicle)
            if status != 1:
                if status == "missing url":
                    return Response("Image URL is required", status=HTTP_400_BAD_REQUEST)
                return Response(status, status=HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Vehicle Created successfully",
                         "vehicle_basic": new_vehicle_data}, status=HTTP_201_CREATED)
