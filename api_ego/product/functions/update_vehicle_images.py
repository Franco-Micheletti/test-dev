"""
"""
from ..models import VehicleImage
from ..functions.create_vehicle_images import create_vehicle_images


def update_vehicle_images(image_list, vehicle):
    """
    - Takes a vehicle object
    - Takes the images_data in this format:

    [
        {
            "url": "https://test/images/fake/1.png",

            "title": "image title 1",

            "detail": "image detail 1"
        },
        {
            "url": "https://test/images/fake/1.png",

            "title": "image title 2",

            "detail": "image detail 2"
        }
    ]
    """

    vehicle_images = VehicleImage.objects.filter(vehicle=vehicle)

    for image in vehicle_images:
        image.delete()

    status = create_vehicle_images(image_list=image_list, vehicle=vehicle)

    return status
