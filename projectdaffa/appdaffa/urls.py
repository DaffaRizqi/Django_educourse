from django.urls import path
from appdaffa import views

urlpatterns = [
    path('', views.index, name='index'),
]