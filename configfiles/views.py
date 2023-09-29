from django.shortcuts import render, redirect
from django.views import View
from django.http import Http404

from .forms import LocationModelForm
from .models import Location
from users.models import User

# Create your views here.
class Index(View):
    def get(self, request):
        
        context = {
        }
        return render(request, 'configfiles/index.html', context)

class ConfigFilesLocations(View):
    def get(self, request):
        
        locations = Location.objects.filter(user=request.user)
        
        context = {
            'model_name': 'Location',
            #'create_view': 'configfiles:create_location',
            'create_view': 'configfiles:show_modal',
            'modal_target': 'location_modal',
            'locations': locations
        }
        return render(request, 'configfiles/view_locations.html', context)
    
    def post(self, request, pk):

        context = {

        }
        #return redirect('configfiles:view_create_locations')    
        return redirect('configfiles:view_locations')

class ConfigFilesCreateLocation(View):
    def get(self, request):

        location_form = LocationModelForm()
        context = {
            'form': location_form

        }
        print('create location')
        return render(request, 'configfiles/create_location.html', context)

class ConfigFilesLocation(View):
    def get(self, request, pk):

        mode = request.GET.get('mode', None)
        if mode is None:
            mode = 'view'

        context = {
            'mode': mode,
            
        }
        return render(request, 'configfiles/view_location.html', context)
    
    def delete(self, request, pk):

        return redirect('configfiles:view_locations')
    
    def post(self, request, pk):

        return redirect('configfiles:view_locations')
    
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
    
def delete_location(request,pk):
    
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    location = Location.objects.get(id=pk)
    location.delete()

    locations = Location.objects.filter(user=request.user)
    context = {
        'locations': locations
    }

    return render(request, 'configfiles/partials/location_list.html', context)

def show_location_form(request):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    print('show location')
    location_form = LocationModelForm()
    context = {
        'form': location_form,
        'add_location': 'configfiles:add_location',

    }

    return render(request, 'configfiles/partials/location_form.html', context)
    
def add_location(request):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    locations = Location.objects.filter(user=request.user)
    context = {
        'locations': locations
    }
    return render(request, 'configfiles/partials/location_list.html', context)
