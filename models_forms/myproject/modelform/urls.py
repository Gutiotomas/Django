from . import views
from django.urls import path
from django.contrib import admin

urlpattern = [
    path('home2/', views.form_view2),
]