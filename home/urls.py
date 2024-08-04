from django.contrib import admin
from django.urls import path
from home import views 
from .views import index , contact_view

urlpatterns = [
    # path('', index, name='index'),
    path('', contact_view, name='index'),
]