from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('receiveData', views.receiveData, name='receiveData'),
    path('getSensorData', views.getSensorData, name='getSensorData'),
]
