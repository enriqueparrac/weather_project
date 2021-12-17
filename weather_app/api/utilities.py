# -*- coding: utf-8 -*-
from decouple import config
import requests
import datetime

def get_fahrenheith(temp):
    return (temp * 9 / 5) + 32


def get_data_api(api_response_json):
    data = []
    try:
        location_name = '%s, %s' % (
            api_response_json['name'], 
            api_response_json['sys']['country']
        )
        temp_c = round(api_response_json['main']['temp'] / 10, 2)
        temp_f = round(get_fahrenheith(temp_c), 2)
        temperature = '[%s C, %s F]' % (
            temp_c, 
            temp_f
        )
        wind = '%s %s' % (
            api_response_json['wind']['speed'], 
            'm/s'
        )
        humidity = '%s %s' % (
            api_response_json['main']['humidity'], 
            '%'
        )
        cloudiness = api_response_json['weather'][0]['description'].capitalize()
        pressure = '%s %s' % (
            api_response_json['main']['pressure'], 
            'hpa'
        )
        geo_coordinates = '[%s, %s]' % (
            api_response_json['coord']['lat'], 
            api_response_json['coord']['lon']
        )
        requested_time = str(datetime.datetime.now())[:19]

        temp_fl_c = round(api_response_json['main']['feels_like'] / 10, 2)
        temp_fl_f = round(get_fahrenheith(temp_fl_c), 2)
        temp_min_c = round(api_response_json['main']['temp_min'] / 10, 2)
        temp_min_f = round(get_fahrenheith(temp_min_c), 2)
        temp_max_c = round(api_response_json['main']['temp_max'] / 10, 2)
        temp_max_f = round(get_fahrenheith(temp_max_c), 2)
        item_forecast = {
            'feels_like': '[%s C, %s F]' % ( temp_fl_c, temp_fl_f ),
            'temp_min': '[%s C, %s F]' % ( temp_min_c, temp_min_f ),
            'temp_max': '[%s C, %s F]' % ( temp_max_c, temp_max_f )
        }
        list_forecast = []
        list_forecast.append(item_forecast)

        item_data = {
            'location_name': location_name,
            'temperature': temperature,
            'wind': wind,
            'cloudiness': cloudiness,
            'pressure': pressure,
            'humidity': humidity,
            'geo_coordinates': geo_coordinates,
            'requested_time': requested_time,
            'forecast': list_forecast
        }
        data.append(item_data)
    except Exception as e:
        print(str(e))
    return data


def get_weather(city, country):
    json = []
    api_data = []
    try:
        WEATHER_API_URL = config('WEATHER_API_URL')
        WEATHER_API_ID = config('WEATHER_API_ID')
        URL = '%sq=%s,%s&appid=%s' % (WEATHER_API_URL, city, country, WEATHER_API_ID)
        api_response = requests.get(URL)
        api_response_json = api_response.json()
        api_data = get_data_api(api_response_json)

        item = {
            'msg': 'Successful API',
            'success': True,
            'result': api_data
        }
    except Exception as e: 
        item = {
            'msg': str(e),
            'success': False,
            'result': api_data,
        }
    json.append(item)
    return json


def get_weather_error():
    json = []
    item = {
        'msg': 'It is necessary to indicate the city and the country',
        'success': False,
        'result': []
    }
    json.append(item)
    return json 