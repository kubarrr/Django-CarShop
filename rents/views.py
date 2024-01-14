from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from cars.models import Car
from .forms import RentForm
from .models import Rent

# Create your views here.
def rent(request, car_pk):
    car=get_object_or_404(Car, pk=car_pk)

    # if car.added_by==request.user:
    #     return redirect('individuals:index')

    if request.method=='POST':
        form=RentForm(request.POST)

        if form.is_valid():
            rent = form.save(commit=False)
            rent.car=car
            rent.owner= car.added_by
            rent.buyer = request.user
            rent.save()

            return render(request, 'rent_confirmation.html', {'email': car.added_by.email})
            # return redirect('rents:rent_confirmation', {'car_pk': car.pk})
            # return redirect('cars:detail', pk=car_pk)
    else:
        form=RentForm()
    return render(request, 'renting.html',{
        'form': form,
        'car': car,
        'owner' :car.added_by,
        'buyer': request.user
    })

# def rent_confirmation(request, car_pk):
#     car = get_object_or_404(Car, pk=car_pk)
#     return render(request, 'rent_confirmation.html', context={
#         'car': car
#     })




