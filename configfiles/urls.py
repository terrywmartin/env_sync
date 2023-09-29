from django.contrib import admin
from django.urls import path

from . import views

app_name = 'configfiles'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('locations/', views.ConfigFilesLocations.as_view(), name='view_locations'),
    path('locations/get', views.get_locations, name='get_locations'),
    path('locations/create', views.add_location, name='create_location'),
    
    path('locations/delete/<uuid:pk>', views.delete_location, name='delete_location'),
    #path('locations/create', views.ConfigFilesCreateLocation.as_view(), name='create_location'),
    path('locations/<uuid:pk>', views.ConfigFilesLocation.as_view(), name='view_delete_edit_location'),
    

]
