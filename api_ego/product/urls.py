from django.urls import path
from . import views

urlpatterns = [

    # Create vehicle
    path("vehicle/create", views.CreateVehicle.as_view()),

]
