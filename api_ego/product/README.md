# PRODUCT API

## CREATE VEHICLE ENDPOINT

The following endpoint uses the POST method to create a new vehicle with the data provided in the request body.

The features and the images are not required to create a new vehicle.

```
URL : vehicle/create
```
### REQUEST BODY EXAMPLE
```json
{
    "name": "Hilux Conquest",
    "type": "Pickups",
    "model": "Conquest",
    "brand": "Toyota",
    "date": "2023-06-12",
    "price": 19000000,
    "features":[
                    ["seguridad","7 airbags: frontales (conductor y acompañante), de rodilla (conductor), laterales (x2) y de cortina (x2)"],
                    ["confort","Audio con pantalla táctil de 8“ y Control de velocidad crucero"],
                    ["exterior","Faros delanteros halógenos con regulación en altura y Sistema 'Follow me home'"],
                    ["transmision","Manual de 6 velocidades. Traccion 4x2"]
                ],
    "images":[  
                {
                    "url":"https://test/images/fake/1.png",
                    "title":"image title 1",
                    "detail":"image detail 1"
                },
                {
                    "url":"https://test/images/fake/1.png",
                    "title":"image title 2",
                    "detail":"image detail 2"
                }
    
            ]
}
```
## SPECIFIC VEHICLE ENDPOINT

The following endpoints uses the GET , PUT and DELETE methods to modify , eliminate or get the data of a specific vehicle with the ID provided in the url.

```
URL : specific_vehicle/id=<int>
```

### METHODS

- GET
- PUT
- DELETE

### PARAMETERS

- id

In order to perform a PUT on a specific vehicle , the endpoint takes a body in JSON format that will be used to update the current data of one vehicle with the new data provided in the body of the request.

The same JSON used for creating a new object should be use for the PUT method , and also both the features and images are not required for the update.

If features or images are not specified in the request, the current data of the vehicle will be used.
