# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from weather_app.api.utilities import (
    get_weather,
    get_weather_error,
)


class GetWeatherAPIView(APIView):
    def get(self, request, *args, **kwargs):
        weather_json = list()        
        city = request.GET.get('city', '')
        country = request.GET.get('country', '')
        if len(city) >= 1 and len(country) >= 1:
            weather_json = get_weather(city, country)
        else:
            weather_json = get_weather_error()                

        return Response(weather_json)