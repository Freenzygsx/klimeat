from django.urls import path
from weather import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/<str:city>', views.getWeather, name='weather')
]
