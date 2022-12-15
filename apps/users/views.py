from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import UserForm
from .models import Users

class Registro(CreateView):
    model = Users 
    template_name = "users/register.html"
    form_class = UserForm

    def get_success_url(self):
        return reverse('login')
