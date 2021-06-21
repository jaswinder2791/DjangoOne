from django.shortcuts import render
from MyEcommerce import settings
from .models import Item

# Create your views here.
def myappfunc(request):
    data = Item.objects.all()
    print(data)
    return render(request, 'website.html', {'data':data, 'media_url':settings.MEDIA_URL})

def addtocart(request):
    title = request.POST.get("data_button", None)
    data = Item.objects.all()
    return render(request, 'addtocart.html', {'data':data, 'media_url':settings.MEDIA_URL, 'title':title} )

def payment(request):
    title = request.POST.get("data_button", None)
    data = Item.objects.all()
    return render(request, 'payment.html', {'data':data, 'media_url':settings.MEDIA_URL, 'title':title})

def checkout(request):
    title = request.POST.get("data_button", None)
    data = Item.objects.all()
    name = request.POST.get("name")
    email = request.POST.get("email")
    address = request.POST.get("address")
    number = request.POST.get("number")
    return render(request, 'checkout.html', {'data':data, 'media_url':settings.MEDIA_URL, 'title':title,
                                            'name':name, 'email':email, 'address':address, 'number':number})

