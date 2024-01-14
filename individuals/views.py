from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from cars.models import Car

#Główny widok do wyświetlania własnych samochodów
@login_required
def index(request):
    cars=Car.objects.filter(added_by=request.user)
    context={
        'cars': cars,
    }
    return render(request, 'individuals/index.html', context)


