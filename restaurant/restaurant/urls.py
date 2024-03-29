"""restaurant URL Configuration

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
from rest.views import dish_list, dish_get, dish_post, dish_put, dish_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dishes/', dish_list),
    path('dishes/<int:pk>', dish_get),
    path('dishes/create/', dish_post),
    path('dishes/update/', dish_put),
    path('dishes/<int:pk>/delete/', dish_delete),
]
