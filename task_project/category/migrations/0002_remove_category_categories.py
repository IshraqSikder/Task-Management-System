# Generated by Django 5.0.1 on 2024-01-11 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='categories',
        ),
    ]