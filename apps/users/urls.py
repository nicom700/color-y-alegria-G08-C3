from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name="users"

urlpatterns = [
    path('register/', views.Registro.as_view(), name="register"),
    path('profile/', views.Profile, name='profile'),
]