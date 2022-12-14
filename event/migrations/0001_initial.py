# Generated by Django 3.2.16 on 2022-11-08 09:37

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Event Title')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('date', models.DateField(verbose_name='Event Date')),
                ('destination', models.CharField(max_length=200, verbose_name='Event Destination')),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Event Image')),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(default=0, verbose_name='Event Price')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attendees', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
