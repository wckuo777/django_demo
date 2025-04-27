"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import include, path
from . import views 
# from django.views.generic import RedirectView
urlpatterns = [
     # 讓首頁 "/" 自動導向 "/charts/"
     # path('', RedirectView.as_view(url='/charts/', permanent=False)),
    path('', views.index, name='index'),  # 首頁顯示功能選單
    path('', include('demo_charts.urls', namespace='demo_charts')),
    path('admin/', admin.site.urls)
]

# 當遇到找不到的網址時，跳回首頁 django no wildcard
def redirect_to_index(request, exception=None):
    return redirect('index')

handler404 = 'mysite.urls.redirect_to_index'
