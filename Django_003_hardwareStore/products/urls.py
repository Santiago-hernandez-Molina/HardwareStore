from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'products'
urlpatterns = [
    path('',views.list, name="list")
]