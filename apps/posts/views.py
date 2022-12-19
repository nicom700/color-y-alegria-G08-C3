from unicodedata import category
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from .forms import PostForm

from slugify import slugify 

from apps.posts.models import Posts
from apps.categories.models import Categories

# Create your views here.
class Index(ListView):
    template_name = 'posts/index1.html'
    model = Posts
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        posts = Posts.objects.all()
        categories = Categories.objects.all()
        return {'posts':posts, 'categories':categories}

    #def get_queryset(self):
    #    productos = Posts.objects.all()
     #   categories = Categories.objects.all()
        #return productos.order_by('-id')
      #  return categories.order_by('-id')

def Create(request):
    form = PostForm()
    categories = Categories.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.slug = slugify(post.title)
            post.image = request.FILES.get('image')
            post.save()            
            return redirect('posts:index')

    form_ = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'posts/create.html', form_)

def Edit(request, pk):
    post = Posts.objects.get(pk=pk)
    form = PostForm(instance=post)
    categories = Categories.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = request.POST['title']
            post.slug = slugify(request.POST['title'])
            post.body = request.POST['body']
            post.category = Categories.objects.get(id=request.POST['category'])
            post.save()
            return redirect('posts:index')
    
    form_ = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'posts/edit.html', form_)

class Delete(DeleteView):
    model = Posts

    def get_success_url(self):
        return reverse('posts:index')