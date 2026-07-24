from django.shortcuts import render
from .models import Service
from .models import User
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



def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User(
            name=name,
            mobile=mobile,
            email=email,
            password=password
        )

        user.save()

        return render(request, "mywebsite/register.html", {
            "message": "Registration Successful"
        })

    return render(request, "mywebsite/register.html")