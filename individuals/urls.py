from django .urls import path
from . import views

app_name='individuals'

urlpatterns=[
    path('', views.index, name='index'),
]