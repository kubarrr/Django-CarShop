from django.db import models
from django.contrib.auth.models import User

from cars.models import Car

class Rent(models.Model):
    car=models.ForeignKey(Car, related_name='rents', on_delete=models.CASCADE)
    owner=models.ForeignKey(User, related_name='sell', on_delete=models.CASCADE, default=1)
    buyer = models.ForeignKey(User, related_name='buy', on_delete=models.CASCADE, default=1)
    start=models.DateTimeField()
    end=models.DateTimeField()
    message=models.TextField()

    def __str__(self):
        return f"Car: {self.car}, Buyer: {self.buyer}, Start: {self.start}, End: {self.end}"




