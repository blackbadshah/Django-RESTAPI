"""Competition_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from api.views import user_curd,competition_curd,entry_curd


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usercurd/', user_curd),
    path('usercurd/<int:id>', user_curd),
    path('comcurd/', competition_curd),
    path('comcurd/<int:id>', competition_curd),
    path('entcurd/', entry_curd),
    path('entcurd/<int:id>', entry_curd),

]