"""lingomeets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'accounts/',
        include('allauth.urls')
    ),
    path(
        '',
        include('home.urls'),
        name='home.urls'
    ),
    path(
        'event/',
        include('event.urls'),
        name='event.urls'
    ),
    path(
        'review/',
        include('review.urls'),
        name='review.urls'
    ),
    path(
        'user_profile/',
        include('user_profile.urls'),
        name='user_profile.urls'
    ),
]
