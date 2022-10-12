
Shipments Rest Api



## Steps to run Backend:

1. Create and activate virtual enviroment
2. Install pip

3. Run commands in command prompt
```
cd shipments_rest_api
pip install -r requirements.txt
python manage.py runserver
```

## Steps to run Frontend
```
npm install
npm start
```

# Api Reference

### Get all shipments:

```
  GET /api/shipments
```


### Create new shipment:

```
  POST /api/shipments
```
 The request expect body in json format

 body  example:
```
 {
    "shipment_ref": "108",
    "delivery_date": "12.12.2022",
    "delivery_town": "Sofia",
    "bayer": "Peter Petrov",
    "seller": "Ivan Nikolov",
    "description": "Some simple description"
  }
```


### Edit existing shipment

```
  PUT /api/shipments/{id}
```
 The request expect body in json format

body example:
```
  {
    "shipment_ref": "108",
    "delivery_date": "12.12.2022",
    "delivery_town": "Sofia",
    "bayer": "Peter Petrov",
    "seller": "Ivan Nikolov",
    "status": "In progress",
    "description": "Some simple description"
  }
```

### Delete existing shipment. 

```
  DELETE /api/shipments/{id}
```


