from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'products'
urlpatterns = [
    path('',views.list, name="list"),
    path('sell',views.register_product , name="register_product"),
    path('filter_by_category/<int:id>/', views.filter_by_category, name="filter_by_category"),
    path('detail/<int:id>/', views.detail, name="detail_category"),
]