from django.shortcuts import render,redirect
from .models import Service
from .models import User
from .decorators import login_required
from django.contrib import messages
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

        name = request.POST["name"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Check if email already exists
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email already registered.")
            return redirect("register")

        User.objects.create(
            name=name,
            mobile=mobile,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful! Please login.")

        return redirect("login")

    return render(request, "mywebsite/register.html")  
def login(request):

    # If user is already logged in, send them to dashboard
    if "user_id" in request.session:
        return redirect("dashboard")

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(
                email=email,
                password=password
            )

            request.session["user_id"] = user.user_id
            request.session["name"] = user.name

            return redirect("dashboard")

        except User.DoesNotExist:
            return render(
                request,
                "mywebsite/login.html",
                {"message": "Invalid Email or Password"}
            )

    return render(request, "mywebsite/login.html")

@login_required
def dashboard(request):

    if "user_id" not in request.session:
        return redirect("login")

    context = {

        "name": request.session["name"]

    }

    return render(request,
                  "mywebsite/dashboard.html",
                  context)
@login_required
def profile(request):

    # Check if user is logged in
    if "user_id" not in request.session:
        return redirect("login")

    # Read user_id from session
    user_id = request.session["user_id"]

    # Fetch user from database
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return redirect("login")

    # Send data to template
    context = {
        "user": user
    }

    return render(request,
                  "mywebsite/profile.html",
                  context)

@login_required
def edit_profile(request):

    user = User.objects.get(
        user_id=request.session["user_id"]
    )

    if request.method == "POST":

        user.name = request.POST["name"]

        user.mobile = request.POST["mobile"]

        user.save()

        request.session["name"] = user.name

        return redirect("profile")

    return render(
        request,
        "mywebsite/edit_profile.html",
        {"user": user}
    )
@login_required
def change_password(request):

    if request.method == "POST":

        current = request.POST["current_password"]
        new = request.POST["new_password"]
        confirm = request.POST["confirm_password"]

        user = User.objects.get(
            user_id=request.session["user_id"]
        )

        if user.password != current:
            # Show error message
            ...

        elif new != confirm:
            # Show error message
            ...

        else:
            user.password = new
            user.save()
            # Show success message
            ...

    return render(request, "mywebsite/change_password.html")

def logout(request):

    request.session.flush()

    messages.success(request, "Logged out successfully.")

    return redirect("login")