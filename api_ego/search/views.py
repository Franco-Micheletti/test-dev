"""
Search views
"""
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from product.models import Vehicle
from product.serializers import VehicleSerializer


class Search(APIView):
    """
    Search endpoint with order_by parameter.
    GET method allowed.
    """

    def get(self, request, vehicle_type='all', order_by=None):
        """
        Returns a list of vehicles based on the search parameters.

        **Vehicle type options**
        ```
            'all'
            'auto'
            'SUVs'
            'pickups'
        ```
        **Order by options**
        ```
            'date'
            '-date'
            'price'
            '-price'  
        ```
        """

        if order_by is not None:
            if str(order_by) in ['-price', 'price', 'date', '-date']:
                if vehicle_type.lower() == 'all':
                    result = Vehicle.objects.all().order_by(str(order_by).lower())
                else:
                    result = Vehicle.objects.filter(
                        type__icontains=str(vehicle_type).lower()).order_by(str(order_by).lower())
            else:
                return Response("order_by is not valid", status=HTTP_400_BAD_REQUEST)
        elif vehicle_type.lower() == 'all':
            result = Vehicle.objects.all()
        else:
            result = Vehicle.objects.filter(
                type__icontains=str(vehicle_type).lower())

        vehicles_data = VehicleSerializer(result, many=True).data

        return Response(vehicles_data, status=HTTP_200_OK)
