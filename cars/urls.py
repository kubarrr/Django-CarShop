from django.urls import path

from . import views

app_name='cars'

urlpatterns=[
    path('', views.cars, name='cars'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]