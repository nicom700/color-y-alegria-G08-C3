from django.shortcuts import render

from apps.categories.models import Categories

def index(request):
    template_name = 'index.html'
    categories = Categories.objects.all()

    return render(request, template_name, {'categories': categories})

def nosotros(request):
    template_name = 'nosotros/nosotros.html'

    return render(request, template_name)
