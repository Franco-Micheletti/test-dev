from django.urls import path
from . import views

urlpatterns = [

    # Create vehicle
    path("vehicle/create", views.CreateVehicle.as_view()),
    # Get specific vehicle data
    path("specific_vehicle/id=<vehicle_id>", views.SpecificVehicle.as_view()),


]
