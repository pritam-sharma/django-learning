from django.shortcuts import render,redirect
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

def dashboard(request):

    if "user_id" not in request.session:
        return redirect("login")

    context = {

        "name": request.session["name"]

    }

    return render(request,
                  "mywebsite/dashboard.html",
                  context)
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

def edit_profile(request):

    # Check Login
    if "user_id" not in request.session:
        return redirect("login")

    # Logged in user id
    user_id = request.session["user_id"]

    # Fetch user
    user = User.objects.get(user_id=user_id)

    # If Update Button Clicked
    if request.method == "POST":

        user.name = request.POST.get("name")

        user.mobile = request.POST.get("mobile")

        user.save()

        # Update session so dashboard shows latest name
        request.session["name"] = user.name

        return render(
            request,
            "mywebsite/edit_profile.html",
            {
                "user": user,
                "message": "Profile Updated Successfully"
            }
        )

    return render(
        request,
        "mywebsite/edit_profile.html",
        {
            "user": user
        }
    )
def change_password(request):

    # Check Login
    if "user_id" not in request.session:
        return redirect("login")

    # Fetch Logged-in User
    user = User.objects.get(user_id=request.session["user_id"])

    if request.method == "POST":

        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        # Check Current Password
        if user.password != current_password:

            return render(
                request,
                "mywebsite/change_password.html",
                {
                    "message": "Current Password is Incorrect"
                }
            )

        # Check New Password & Confirm Password
        if new_password != confirm_password:

            return render(
                request,
                "mywebsite/change_password.html",
                {
                    "message": "New Password and Confirm Password do not match"
                }
            )

        # Update Password
        user.password = new_password
        user.save()

        return render(
            request,
            "mywebsite/change_password.html",
            {
                "success": "Password Changed Successfully"
            }
        )

    return render(request, "mywebsite/change_password.html")
def logout(request):

    # Remove all session data
    request.session.flush()

    # Redirect to Login Page
    return redirect("login")