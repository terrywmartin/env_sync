from django.contrib import admin
from django.urls import path

from . import views

app_name = 'configfiles'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

]
