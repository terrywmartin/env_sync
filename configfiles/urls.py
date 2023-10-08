from django.contrib import admin
from django.urls import path

from . import views

app_name = 'configfiles'

urlpatterns = [
    #path('', views.Index.as_view(), name='index'),

    path('projects/', views.ConfigFilesProjects.as_view(), name='view_projects'),
    path('projects/<uuid:pk>', views.ConfigFilesProject.as_view(), name='view_project'),
    path('projects/get', views.get_projects, name='get_projects'),
    path('projects/create', views.create_project, name='add_project'),
    path('projects/delete/<uuid:pk>', views.delete_project, name='delete_project'),

    path('projects/<uuid:project_id>/files/get', views.get_project_files, name='get_project_files'),

    path('locations/', views.ConfigFilesLocations.as_view(), name='view_locations'),
    path('locations/get', views.get_locations, name='get_locations'),
    path('locations/create', views.add_location, name='add_location'),
    
    path('locations/delete/<uuid:pk>', views.delete_location, name='delete_location'),
    #path('locations/create', views.ConfigFilesCreateLocation.as_view(), name='create_location'),
    path('locations/<uuid:pk>', views.ConfigFilesLocation.as_view(), name='view_location'),
    path('locations/<uuid:location_id>/files/get', views.get_location_files, name='get_location_files'),
    
    path('files', views.ConfigFilesFiles.as_view(), name='view_files'),
    path('files/<uuid:pk>/delete', views.delete_file, name='delete_file'),
    path('files/<uuid:pk>', views.ConfigFilesFile.as_view(), name='view_file'),
    path('files/add', views.ConfigFilesAddFile.as_view(), name='add_file'),
    path('files/upload', views.upload_file, name='uploader'),


]
