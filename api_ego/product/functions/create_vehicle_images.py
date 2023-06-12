"""
Contains a function that creates the vehicle images with the provided data.
"""
from ..models import VehicleImage


def create_vehicle_images(image_list, vehicle):
    """
    - Takes a vehicle object
    - Takes an image list with format:

    [  
        {
            "url":"https://test/images/fake/1.png",

            "title":"image title",

            "detail":"image detail"
        },

        {
            "url":"https://test/images/fake/2.png",

            "title":"image title 2",

            "detail":"image detail 2 "
        }

    ]
    """
    try:
        for image in image_list:
            url = image.get("url")
            if url is not None:
                VehicleImage.objects.create(
                    vehicle=vehicle,
                    url=image.get("url"),
                    title=image.get("title", None),
                    detail=image.get("detail", None),
                )
            else:
                return "missing url"
        return 1
    except Exception as error:
        return error
