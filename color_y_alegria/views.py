from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    
    return render(request, template_name)

def nosotros(request):
    template_name = 'nosotros/nosotros.html'

    return render(request, template_name)