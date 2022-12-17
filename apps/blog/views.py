from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from apps.comments.forms import CommentForm
from apps.comments.models import Comments

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
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.user_id = request.user.id
            form.save()

            return redirect('blog:show', slug = slug)
    else:
        form = CommentForm()

    categories = Categories.objects.filter(id = post.category_id)
    comments = Comments.objects.filter(post_id = post.id)
    context = {'post': post, 'categories': categories, 'comments': comments, 'form': form}

    return render(request, 'blog/show.html', context)

