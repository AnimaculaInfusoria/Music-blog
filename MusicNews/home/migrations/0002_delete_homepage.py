# Generated by Django 3.2.11 on 2022-01-14 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]