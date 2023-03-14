# Generated by Django 4.1.7 on 2023-03-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_blog_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('favicon', models.ImageField(blank=True, default='', null=True, upload_to='images')),
                ('logo', models.ImageField(blank=True, default='', null=True, upload_to='images')),
                ('short_description', models.TextField(blank=True, max_length=255, null=True)),
                ('location_map', models.TextField(blank=True, null=True)),
                ('footer_text_copyright', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('footer_copyright_url', models.URLField(blank=True, default='', null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meta_title', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('meta_keyword', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'verbose_name': 'Company Information',
                'verbose_name_plural': 'Company Information',
            },
        ),
    ]