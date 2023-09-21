# VEHICLES API

This is a API created with Python 3.10.4 and Django Rest Framework.
It has different features such as:
- Ordering by
- Filter by Type
- CRUD
- Swagger UI

# HOW TO TEST THIS API

## - STEP 1 - 

Open cmd in your windows machine select the folder where you want the repository to be extracted at and execute the next command:

```
git clone https://github.com/Franco-Micheletti/test-dev
```

## - STEP 2 - 

Create .env file with the SECRET_KEY variable inside for security purposes.
To generate a new SECRET_KEY do the following:
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit
```
Open an integrated terminal on the repository folder and execute the following command in order to install all the modules required for the project:
```
pip install -r requirements.txt
```

## - STEP 3 - 

Open an integrated terminal on the api_ego folder that contains the manage.py file and execute the following command:
```
python manage.py runserver
```

### AND THAT'S IT ! NOW YOU ARE READY TO TEST THE API WITH THE ENDPOINTS AVAILABLE

# SWAGGER UI

- /docs/

# ENDPOINTS

## Product
- /vehicle/create - [POST]
- /specific_vehicle/id=<vehicle_id> - [GET] [PUT] [DELETE]
## Search
- /search/type=<vehicle_type>&order_by=<order_by> - [GET]
- /search/type=<vehicle_type> - [GET]

# TESTING

In order to ensure that the API is working as expected i have created a series of tests for each endpoint that can be run before working with the API or touching any part of the code.

Open an integrated terminal on the api_ego folder that contains the manage.py file and execute the following command:
```
python manage.py test
```
Result should be OK if all the test were successful.