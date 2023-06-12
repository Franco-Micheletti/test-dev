# API TEST - EGO

This a API created with Python 3.10.4 and Django Rest Framework for the backend test of ego.

# HOW TO TEST THIS API

## - STEP 1 - 

Open cmd in your windows machine select the folder where you want the repository to be extracted at and execute the next command:

```
git clone https://github.com/Franco-Micheletti/test-dev
```

## - STEP 2 - 

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

# ENDPOINTS

- /vehicle/create - [POST]
- /specific_vehicle/id=<vehicle_id> - [GET] [PUT] [DELETE]