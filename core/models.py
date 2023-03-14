from django.db import models
from datetime import date
# Create your models here.
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    featured_image = models.ImageField(upload_to='blog')
    description = RichTextField()
    readtime = models.CharField(
        max_length=10, help_text='eg: 5 min', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'


class CompanyInfo(models.Model):
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    favicon = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    logo = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    short_description = models.TextField(max_length=255, blank=True, null=True)
    location_map = models.TextField(null=True, blank=True)
    footer_text_copyright = models.CharField(
        max_length=100, null=True, blank=True, default='')
    footer_copyright_url = models.URLField(
        default='', null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    meta_title = models.CharField(
        max_length=255, default='', null=True, blank=True)
    meta_keyword = models.CharField(
        max_length=255, default='', null=True, blank=True)
    meta_description = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Company Information'
        verbose_name_plural = 'Company Information'
