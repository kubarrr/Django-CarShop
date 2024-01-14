from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from django.db.models import Q

from .forms import NewCarForm, EditCarForm
from .models import Car, Category

# Create your views here.
def detail(request, pk):
    car=get_object_or_404(Car, pk=pk)
    context={
        'car': car
    }

    return render(request, 'car/detail.html', context)

@login_required()
def new(request):
    if request.method=='POST':
        form=NewCarForm(request.POST, request.FILES)

        if form.is_valid():
            car=form.save(commit=False)
            car.added_by=request.user
            car.save()

            return redirect('cars:detail', pk=car.id)
    else:
        form=NewCarForm()

    context={
        'form': form,
        'title': 'New car',
    }

    return render(request, 'car/form.html', context)

@login_required()
@user_passes_test(lambda u: u.is_superuser)
def edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method=='POST':
        form=EditCarForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()

            return redirect('cars:detail', pk=car.id)
    else:
        form=EditCarForm(instance=car)

    context={
        'form': form,
        'title': 'Edit car',
    }

    return render(request, 'car/form.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()

    return redirect('individuals:index')

#Tutaj tworzę listę samochodów spełniających dane kryteria wyszukiwania
def cars(request):
    search=request.GET.get('search', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    cars = Car.objects.all()

    if search:
        cars=cars.filter(Q(name__icontains=search) | Q(brand__icontains=search) | Q(transmission__icontains=search)|Q(description__icontains=search))

    if category_id:
        cars = cars.filter(category_id=category_id)

    context={
        'cars': cars,
        'search': search,
        'categories': categories,
        'category_id': int(category_id)
    }


    return render(request, 'car/cars.html', context)



