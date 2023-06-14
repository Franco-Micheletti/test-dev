path('search/type=<vehicle_type>&order_by=<order_by>',
         views.SearchWithOrderBy.as_view()),
    path('search/type=<vehicle_type>', views.SearchWithOutOrderBy.as_view())

# SEARCH API

Returns data in JSON format with x amount of elements.
```
URL : /search/type=<vehicle_type>&order_by=<order_by>
```
Takes two optional parameters:

- type : 
    - The vehicle type 
    - Default value is 'all'
- order_by : 
    - A string that indicates how we want to order the data.
    - Default value is None
### VEHICLE TYPE OPTIONS:
`
'all'
'auto'
'SUVs'
'pickups'
`
### ORDER BY OPTIONS:
`
'date'
'-date'
'price'
'-price'
`

Without ' - ' means ASC and the lower prices or the oldest date will be at the top.

With ' - ' means DESC and the highest prices or the most recent date will be at the top.

## RESPONSE DATA EXAMPLE

```json
[
    {
        "id": 13,
        "name": "Yaris",
        "type": "Auto",
        "model": "Yaris",
        "brand": "Toyota",
        "price": 1038900.0,
        "date": "2020-06-23"
    },
    {
        "id": 12,
        "name": "Etios",
        "type": "Auto",
        "model": "Etios",
        "brand": "Toyota",
        "price": 815900.0,
        "date": "2019-06-23"
    }
]
```

