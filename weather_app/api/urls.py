# -*- coding: utf-8 -*-
from rest_framework import routers
from django.conf.urls import url
from weather_app.api.views import (
    GetWeatherAPIView,
)

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^weather', GetWeatherAPIView.as_view(), name='weather'),
]

urlpatterns += router.urls