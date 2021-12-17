# Weather Project

## Instructions to run the project

requirement python >= 3.6 


#### 1. Clone gitHub project
https://github.com/enriqueparrac/weather_project.git

cd /weather_project


#### 2. Create a virtual environment in python
python -m venv environmentName


#### 3. Download the project libraries
pip install -r requirements.txt


### 4. Run local Django server
python manage.py runserver


### 5. Write the following URL in the browser including 2 parameters: the city and the country.
http://127.0.0.1:8000/weather/?city=Bogota&country=co

http://127.0.0.1:8000/weather/?city=Mexico&country=mx

http://127.0.0.1:8000/weather/?city=Argentina&country=ar


### 6. The API will return the following JSON
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "msg": "Successful API",
        "success": true,
        "result": [
            {
                "location_name": "Bogota, CO",
                "temperature": "[29.09 C, 84.36 F]",
                "wind": "3.6 m/s",
                "cloudiness": "Scattered clouds",
                "pressure": "1026 hpa",
                "humidity": "55 %",
                "geo_coordinates": "[4.6097, -74.0817]",
                "requested_time": "2021-12-17 09:49:47",
                "forecast": [
                    {
                        "feels_like": "[29.01 C, 84.22 F]",
                        "temp_min": "[29.09 C, 84.36 F]",
                        "temp_max": "[29.09 C, 84.36 F]"
                    }
                ]
            }
        ]
    }
]


### 7. In another case, the API will return the following JSON
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "msg": "It is necessary to indicate the city and the country",
        "success": false,
        "result": []
    }
]
