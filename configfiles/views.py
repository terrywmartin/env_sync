from django.shortcuts import render, redirect
from django.views import View
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import LocationModelForm
from .models import Location, File
from users.models import User

# Create your views here.
""" 
class Index(View):
    def get(self, request):
        
        context = {
        }
        return render(request, 'configfiles/index.html', context)
 """
class ConfigFilesLocations(LoginRequiredMixin, View):
    def get(self, request):
        
        locations = Location.objects.filter(user=request.user)
        form = LocationModelForm()
        context = {
            'model_name': 'Location',
            #'create_view': 'configfiles:create_location',
            'create_view': 'configfiles:add_location',
            'modal_target': 'location_modal',
            'list_target': '#location-list',
            'input_name': 'location_name',
            'placeholder_text': 'Enter a location',
            'button_text': 'Add location',
            'locations': locations,
            'form': form,
            'add_form': True
        }
        return render(request, 'configfiles/view_locations.html', context)
    
 
class ConfigFilesLocation(LoginRequiredMixin, View):
    def get(self, request, pk):

        mode = request.GET.get('mode', None)
        if mode is None:
            mode = 'view'

        location = Location.objects.get(id=pk)
        files = File.objects.filter(location=location)

        context = {
            'mode': mode,
            'location': location,
            'files': files,    
            'view_file': 'configfiles:view_location_file',
            'edit_file': 'configfiles:edit_location_file',
            'delete_file': 'configfiles:delete_location_file',
        }
        return render(request, 'configfiles/view_location.html', context)


class ConfigFilesFiles(LoginRequiredMixin, View):
    def get(self, request):
        
        files = File.objects.filter(user=request.user)
        form = LocationModelForm()
        context = {
            'model_name': 'Location',
            #'create_view': 'configfiles:create_location',
            'create_view': 'configfiles:add_location',
            'modal_target': 'location_modal',
            'list_target': '#location-list',
            'input_name': 'location_name',
            'placeholder_text': 'Enter a location',
            'button_text': 'Add location',
            'locations': files,
            'form': form,
            'add_form': True
        }
        return render(request, 'configfiles/view_locations.html', context)
    
 
class ConfigFilesLocationFile(LoginRequiredMixin, View):
    def get(self, request, location_id, pk):

        mode = request.GET.get('mode', None)
        if mode is None:
            mode = 'view'

        file = File.objects.filter(id=pk)

        context = {
            'mode': mode,
            'files': file,    
        }
        return render(request, 'configfiles/view_location.html', context)

@login_required(login_url='login') 
def get_locations(request):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    locations = Location.objects.filter(user=request.user)
        
    context = {
        'locations': locations
    }
    return render(request, 'configfiles\partials\location_list.html', context)

@login_required(login_url='login')  
def delete_location(request,pk):
    
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    location = Location.objects.get(id=pk)
    location.delete()

    #return render(request, 'configfiles/partials/location_list.html', context)
    return HttpResponse(status=204, headers={'HX-Trigger': 'locationListChanged'})

@login_required(login_url='login')
def add_location(request):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    location_name = request.POST.get('location_name', None)
    if location_name != None:
        location = Location(name=location_name, user=request.user)
        location.save()
    
     #return render(request, 'configfiles/partials/location_list.html', context)
    return HttpResponse(status=201, headers={'HX-Trigger': 'locationListChanged'})

@login_required(login_url='login') 
def get_location_files(request, location_id):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    location = Location.objects.get(id=location_id)
    files = File.objects.filter(location=location)
        
    context = {
        'files': files,
        'location': location,
        'view_file': 'configfiles:view_location_file',
        'edit_file': 'configfiles:edit_location_file',
        'delete_file': 'configfiles:delete_location_file',
    }
    return render(request, 'configfiles/partials/file_list.html', context)

@login_required(login_url='login')  
def delete_location_file(request, location_id, pk):
    
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    
    return HttpResponse(status=204, headers={'HX-Trigger': 'fileListChanged'})
