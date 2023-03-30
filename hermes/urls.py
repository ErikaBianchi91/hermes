"""hermes URL Configuration

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
from django.urls import path, re_path
from app import views

urlpatterns = [
    
    re_path(r'^admin/', admin.site.urls),
    re_path(r'home/', views.home),
    re_path(r'^new/',views.index, name='index'),
    re_path(r'^open/(\d+)/$',views.open, name='open'),
    re_path(r'^kitchen/',views.kitchen, name='kitchen'),
    re_path(r'^cooking/(\d+)/$', views.cookingStarted,  name='cookingStarted'),
    re_path(r'^cooked/(\d+)/$', views.cookingEnded,  name='cookingEnded'),
    re_path(r'^openOrders/',views.showOrderstoDeliver, name='orderstoDeliver'),
    re_path(r'^closeOrder/(\d+)/$',views.closeOrder, name='closeOrder'),
    re_path(r'^cashier/',views.cashierPage, name='cashierPage'),
    re_path(r'^pay/(\d+)/$', views.pay,  name='pay'),
    re_path(r'^clearTable/(\d+)/$', views.clearTable,  name='clearTable'),
    
]
