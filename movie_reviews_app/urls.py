"""movie_reviews_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from movie_reviews.views import *

urlpatterns = [
    path('', root, name="index"),
    path('admin/', admin.site.urls),
    path('signup/', user_signup, name="signup"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('home/', home, name="home"),
    path('movie/', movie_redirect, name="movie_redirect"),
    path('movie/<int:pid>', movies, name="movies"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
