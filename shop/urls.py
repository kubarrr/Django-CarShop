from django.urls import path
from django.contrib.auth import views

from . import views

app_name='shop'

urlpatterns=[
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('confirmation_registration/', views.confirm_registration, name='confirmation_registration'),
    # path('login/', auth_views., name='contact'),
]