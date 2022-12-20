from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import CategoryForm

from apps.categories.models import Categories

# Create your views here.
class Index(ListView):
    template_name = 'categories/index.html'
    model = Categories
    context_object_name = 'categories'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

    def get_queryset(self):
        productos = Categories.objects.all()
        return productos.order_by('-id')

class Create(CreateView):
    model = Categories 
    template_name = 'categories/create.html'
    form_class = CategoryForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

    def get_success_url(self):
        return reverse('categories:index')

class Edit(UpdateView):
    model = Categories
    template_name = 'categories/edit.html'
    form_class = CategoryForm     

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

    def get_success_url(self):
        return reverse('categories:index')

class Delete(DeleteView):
    model = Categories

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

    def get_success_url(self):
        return reverse('categories:index')