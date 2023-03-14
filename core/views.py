from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def index(request):
    featured = Blog.objects.latest('id')
    blogs = Blog.objects.all().order_by('-id')[:6]
    featured_blogs = Blog.objects.filter(is_featured=True).order_by('-id')

    context = {
        'featured': featured,
        'blogs': blogs,
        'featured_blogs': featured_blogs,
    }

    return render(request, 'index.html', context)


def blog_detail(request, blog_slug):
    single_blog = get_object_or_404(Blog, slug=blog_slug)
    blogs = Blog.objects.all().order_by('-id')[:3]
    context = {
        'single_blog': single_blog,
        'blogs': blogs,
    }
    return render(request, 'blog-detail.html', context)
