from django.urls import path 
from .views import CarListView, AddCarView



urlpatterns = [
    path('', CarListView.as_view(), name="car_list"),
    path('add/', AddCarView.as_view(), name="add_car"),
]