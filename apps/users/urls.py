from django.urls import path
<<<<<<< HEAD

from . import views

app_name="users"

urlpatterns = [
    path('register/', views.Registro.as_view(), name="register"),
=======
from . import views

from django.contrib.auth import views as auth_views

app_name='users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
>>>>>>> login
]