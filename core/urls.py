
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blogs, name='blogs'),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='blog-detail'),
]
