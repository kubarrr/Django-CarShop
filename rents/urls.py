from django .urls import path

from . import views

app_name='rents'

urlpatterns=[
    path('renting/<int:car_pk>/', views.rent, name='renting'),
]
