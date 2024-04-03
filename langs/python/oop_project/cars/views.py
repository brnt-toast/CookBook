from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Car

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
        
class AddCarView(CreateView):
    model = Car
    fields = ['brand', 'model']
    template_name = 'cars/add_car.html'
    success_url = reverse_lazy('car_list')