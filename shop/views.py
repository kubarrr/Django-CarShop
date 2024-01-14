from django.shortcuts import render, redirect
from cars.models import Category, Car
from django.shortcuts import HttpResponse

from .forms import SignupForm

# Create your views here.
def index(request):
    cars=Car.objects.all()
    categories=Category.objects.all()
    context={
        'categories': categories,
        'cars': cars,
    }

    return render(request, 'shop/index.html', context)


# from xml.etree import ElementTree as ET
# def contact(request):
#     xml_path = 'shop/templates/shop/info_contact.xml'
#     tree = ET.parse(xml_path)
#     root = tree.getroot()
#
#     owner = root.find('owner').text
#     email = root.find('email').text
#     address = root.find('address').text
#     phone = root.find('phone').text
#
#     context = {
#         'owner': owner,
#         'email': email,
#         'address': address,
#         'phone': phone,
#     }
#
#     return render(request, 'shop/contact.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            request.session['user_data'] = request.POST.dict()  # Zapisz dane w sesji
            return redirect('/confirmation_registration/')  # Przekieruj do potwierdzenia
            #return redirect('/confirming/')  # Przekieruj do potwierdzenia
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'shop/signup.html', context)

def confirm_registration(request):
    user_data = request.session.get('user_data')
    if request.method == 'POST' and user_data:
        form = SignupForm(user_data)
        if form.is_valid():
            form.save()
            del request.session['user_data']
            return redirect('/accounts/login/')
        else:
            return redirect('/signup/')

    context = {
        'email': user_data.get('email') if user_data else None,
        'username': user_data.get('username') if user_data else None,
    }
    return render(request, 'shop/confirmation_registration.html', context)


from lxml import etree
from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    xml_path = 'shop/templates/shop/info_contact.xml'
    xsl_path = 'shop/templates/shop/contact.xsl'


    xml_tree = etree.parse(xml_path)
    xsl_tree = etree.parse(xsl_path)
    transform = etree.XSLT(xsl_tree)
    result_tree = transform(xml_tree)
    result_html = str(result_tree)

    return HttpResponse(result_html, content_type='text/html')




