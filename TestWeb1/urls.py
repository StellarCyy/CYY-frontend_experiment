"""
URL configuration for TestWeb1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
#python manage.py runserver
#python manage.py runserver 0.0.0.0:8000可以在手机上运行
from django.contrib import admin
from django.urls import path,re_path
from TestApp1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    re_path(r'^(?P<page_name>[\w\.-]+)/?$', views.universal_page, name='universal_page'),
]
