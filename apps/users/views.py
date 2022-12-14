from django.urls import reverse
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import UserForm

from apps.users.models import Users

# Create your views here.
class Register(CreateView):
    model = Users
    template_name = 'users/register.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('users:login')