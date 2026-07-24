from django.shortcuts import render
from .models import Service
# Create your views here.
def home(request):
    return render(request, 'mywebsite/home.html')


def about(request):
    return render(request, 'mywebsite/about.html')


def contact(request):
    return render(request, 'mywebsite/contact.html')

def services(request):

    data = Service.objects.all()

    return render(request,
                  'mywebsite/services.html',
                  {'services': data})