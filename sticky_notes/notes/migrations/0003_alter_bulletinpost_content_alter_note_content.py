# Generated by Django 5.0.6 on 2024-06-21 11:44

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_bulletinpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletinpost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]