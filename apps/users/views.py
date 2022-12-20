from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import ProfileForm
from .forms import UserForm
from .models import Users

class Registro(CreateView):
    model = Users 
    template_name = "users/register.html"
    form_class = UserForm

    def get_success_url(self):
        return reverse('login')

def Profile(request):
    user = Users.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            if not request.FILES.get('photo') or request.FILES.get('photo').name == None:
                form = form.save(commit=False)
                form.photo = None

            form.save()
            return redirect('users:profile')

    photo = user.photo
    return render(request, 'users/profile.html', {'photo': photo})
