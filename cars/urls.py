from django.urls import path
from . import views
from . serializers import CarSerializer
from . models import Car

urlpatterns = [
    path('', views.cars_list),
    path('<pk>/', views.car_detail),
]