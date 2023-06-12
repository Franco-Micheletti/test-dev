"""
Product models:

-Vehicle

-Feature Name

-Feature Description

-Feature Couple

-Vehicle Feature

"""
from django.db import models


class FeatureName(models.Model):
    """
    Features Name model.
    """
    name = models.CharField(max_length=300)


class FeatureDescription(models.Model):
    """
    Features Description model.
    """
    description = models.CharField(max_length=2000)


class FeatureCouple(models.Model):
    """
    Contains records of a feature name with their description.
    """
    feature_name = models.ForeignKey(to=FeatureName, on_delete=models.CASCADE)
    feature_description = models.ForeignKey(
        to=FeatureDescription, on_delete=models.CASCADE)


class Vehicle(models.Model):
    """
    Vehicle model
    """
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300, null=True, blank=True)
    model = models.CharField(max_length=300, null=True, blank=True)
    brand = models.CharField(max_length=300, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)


class VehicleFeature(models.Model):
    """
    Many to Many field used to access the features of a 
    vehicle directly if we want to make a specific search 
    of only the features of a specific vehicle.
    """
    vehicle = models.ForeignKey(to=Vehicle, on_delete=models.CASCADE)
    feature = models.ForeignKey(to=FeatureCouple, on_delete=models.CASCADE)


class VehicleImage(models.Model):
    """
    Vehicle Images
    """
    vehicle = models.ForeignKey(to=Vehicle, on_delete=models.CASCADE)
    url = models.URLField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    detail = models.CharField(max_length=2000, null=True, blank=True)
