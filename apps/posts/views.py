from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
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
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.slug = slugify(post.title)
            """ post.category_id = post.category """
            post.save()
            form = PostForm()
            return redirect('posts:index')
    else:
        posts = Posts.objects.all()
        categories = Categories.objects.all()
        context = {'posts':posts, 'categories':categories}
    return render(request, 'posts/create.html', context)

""" class Create(CreateView):
    model = Posts 
    template_name = 'posts/create.html'
    form_class = PostForm

    def get_context_data(self, *args, **kwargs):
        posts = Posts.objects.all()
        categories = Categories.objects.all()
        return {'posts':posts, 'categories':categories}

    def get_success_url(self):
        return reverse('posts:index')

    def form_valid(self, form):
        f = form.save(commit=False)
        print(f)
        f.user_id = self.request.user.id
        f.category_id = f.category
        f.slug = slugify(f.title)
        print(f.category_id)
        f.save()
        return reverse('posts:index')
        #return super().form_valid(f) """

class Edit(UpdateView):
    model = Posts
    template_name = 'posts/edit.html'
    form_class = PostForm     

    def get_success_url(self):
        return reverse('posts:index')

class Delete(DeleteView):
    model = Posts

    def get_success_url(self):
        return reverse('posts:index')