from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.brand} {self.model}'