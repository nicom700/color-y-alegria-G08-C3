from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from apps.posts.models import Posts
from apps.categories.models import Categories

# Create your views here.
class Index(ListView):
    template_name = 'blog/index.html'
    model = Posts
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        posts = Posts.objects.all()
        categories = Categories.objects.all()
        return {'posts':posts, 'categories':categories}

def Show(request, slug):
    post = get_object_or_404(Posts, slug = slug)
    
    #post = Posts.objects.filter(slug=slug)
    categories = Categories.objects.filter(id=post.category_id)
    context = {'post': post, 'categories': categories}
    return render(request, 'blog/show.html', context)