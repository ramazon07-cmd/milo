from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Post, Comment, Contact
from django.db.models import Q
from .forms import CommentForm, CreateContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

# class HomeView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'home.html'
#
#     def get_queryset(self): # tartiblash
#         return self.model.objects.order_by('name')

def get_popular_posts(limit=2):
    return Post.objects.order_by('-views_count')[:limit]

def home(request):
    posts = Post.objects.all()
    popular_posts = Post.objects.order_by('-views_count')[:5]
    popular_posts = get_popular_posts(limit=2)
    famous_posts = Post.objects.order_by('-views_count')[:5]
    famous_posts = get_popular_posts(limit=3)


    context = {
        'posts': posts,
        'popular_posts': popular_posts,
        'famous_posts': famous_posts,
    }

    return render(request, 'home.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    popular_posts = Post.objects.order_by('-views_count')[:5]

    post.views_count += 1
    post.save()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)

    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post).order_by('-created_at')

    context = {
        'post': post,
        'popular_posts': popular_posts,
        'form': form,
        'comments': comments,
    }

    return render(request, 'detail.html', context)

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class CreateContactView(SuccessMessageMixin, CreateView):
	model = Contact
	# fields = ['name', 'email', 'phone', 'message']
	form_class = CreateContactForm
	template_name = 'contact.html'
	success_url = '/'
	success_message = 'Created'

def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(slug__icontains=query) | Q(place__icontains=query)
        )
    return render(request, 'search.html', {'query': query, 'results': results})

def posts(request):
    results = Post.objects.all()
    return render(request, 'posts.html', {'results': results})
