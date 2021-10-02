"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.page_index_view),
    path('admin/', admin.site.urls),
    path('page/2021/', views.page_2021_view),
    # path转换器，匹配page/1、page/2、page/3等等
    path('page/<int:pageNum>', views.page_N_view),
    #匹配http://0.0.0.0:8000/20/mul/40
    #不可匹配http://0.0.0.0:8000/200/mul/400
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.re_view)

]
