from django.contrib import admin
from django.urls import path

from . import views

app_name = 'configfiles'

urlpatterns = [
    #path('', views.Index.as_view(), name='index'),
    path('locations/', views.ConfigFilesLocations.as_view(), name='view_locations'),
    path('locations/get', views.get_locations, name='get_locations'),
    path('locations/create', views.add_location, name='add_location'),
    
    path('locations/delete/<uuid:pk>', views.delete_location, name='delete_location'),
    #path('locations/create', views.ConfigFilesCreateLocation.as_view(), name='create_location'),
    path('locations/<uuid:pk>', views.ConfigFilesLocation.as_view(), name='view_location'),
    
    path('files', views.ConfigFilesFiles.as_view(), name='view_files'),
    path('locations/<uuid:location_id>/files/get', views.get_location_files, name='get_location_files'),
    path('locations/<uuid:location_id>/files/<uuid:pk>/delete', views.delete_location_file, name='delete_location_file'),
    path('locations/<uuid:location_id>/files/<uuid:pk>', views.ConfigFilesLocationFile.as_view(), name='view_location_file'),
    


]
