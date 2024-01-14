from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Car(models.Model):
    category = models.ForeignKey(Category, related_name='cars', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    transmission = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images_cars', blank=True, null=True)
    available_since = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
