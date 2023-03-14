from django.shortcuts import render
from .models import Blog
# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog_detail(request):
    return render(request, 'blog-detail.html')
