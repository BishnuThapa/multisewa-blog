# Generated by Django 4.1.7 on 2023-03-14 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_companyinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyinfo',
            options={'verbose_name': 'General Info', 'verbose_name_plural': 'General Setting'},
        ),
    ]
