from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path(
    "edit-profile/",
    views.edit_profile,
    name="edit_profile"
),
path(
    "change-password/",
    views.change_password,
    name="change_password"
),
path("logout/", views.logout, name="logout"),

]