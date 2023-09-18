from django.contrib import admin
from django.urls import path

from . import views

app_name = 'apikeys'

urlpatterns = [
   # path('', views.Index.as_view(), name='index'),
   path('generate/', views.CreateAPIKey.as_view(), name="CreateAPIKey"),
   path('delete/<uuid:pk>', views.DeleteAPIKey.as_view(), name="DeleteAPIKey"),

]
