from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import LocationModelForm, ConfigFileModelForm
from .models import Location, File, ConfigFile
from users.models import User

# Create your views here.
""" 
class Index(View):
    def get(self, request):
        
        context = {
        }
        return render(request, 'configfiles/index.html', context)
 """

class ConfigFilesProjects(LoginRequiredMixin, View):
    def get(self, request):
        projects = ConfigFile.objects.filter(user=request.user)

        form = ConfigFileModelForm()
        
        context = {
            'model_name': 'Location',
            #'create_view': 'configfiles:create_location',
            'create_view': 'configfiles:add_project',
            'modal_target': 'project_modal',
            'list_target': '#project-list',
            'input_name': 'project_name',
            'placeholder_text': 'Enter a project',
            'button_text': 'Add project',
            'projects': projects,
            'form': form,
            'add_form': True,
            'form_id': 'projectForm',
            'view_url': 'configfiles:view_project',
            'delete_url': 'configfiles:delete_project',
            'col1_header': 'Name',
            'col2_header': '',
            'col3_header': '',
            'col4_header': '',
            'col5_header': '',
            'col6_header': '',
        }
        return render(request, 'configfiles/view_projects.html', context)
    
    
    def post(self, request):
        pass

class ConfigFilesProject(LoginRequiredMixin, View):
    def get(self, request, pk):
        mode = request.GET.get('mode', None)
        if mode is None:
            mode = 'view'

        project = ConfigFile.objects.get(id=pk)
        files = File.objects.filter(config=project)

        context = {
            'mode': mode,
            'project': project,
            'files': files,    
            'location_id': None,
            'project_id': project.id,
            'view_file': 'configfiles:view_file',
            'edit_file': 'configfiles:edit_file',
            'delete_file': 'configfiles:delete_file',
            'next': reverse('configfiles:view_project', args=[project.id]),
            'view_url': 'configfiles:view_project',
            'delete_url': 'configfiles:delete_project',
        }
        return render(request, 'configfiles/view_project.html', context)


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
            'add_form': True,
            'form_id': 'loactionForm',
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
            'items': files,  
            'location_id': location.id,
            'project_id' : None,  
            'view_file': 'configfiles:view_file',
            'edit_file': 'configfiles:edit_file',
            'delete_file': 'configfiles:delete_file',
            'next': reverse('configfiles:view_location', args=[location.id]),
            'view_url': 'configfiles:view_project',
            'delete_url': 'configfiles:delete_project',
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
            'location_id': None,
            'project_id': None,
            'locations': files,
            'form': form,
            'add_form': True,
        
        }
        return render(request, 'configfiles/files.html', context)
    
class ConfigFilesAddFile(LoginRequiredMixin, View):
    def get(self, request):
        location_id = request.GET.get('location_id', None)
        project_id = request.GET.get('project_id', None)
        next = request.GET.get('next', None)
        """  if location_id:
            location = Location.objects.filter(id=location_id)
            locations = [ location ]
        else:
            locations = Location.objects.filter(user=request.user) 
        """
        locations = Location.objects.filter(user=request.user)
        """ if project_id:
            project = ConfigFile.objects.filter(id=project_id)
            projects = [ project ]
        else:
            projects = ConfigFile.objects.filter(user=request.user) """
        projects = ConfigFile.objects.filter(user=request.user)
        
        context = {
            'location_id':  location_id,
            'project_id': project_id,
            'projects':   projects,
            'locations': locations,
            'next': next,
        }
        return render(request, 'configfiles/upload_file.html', context)
    
    def post(self, request):
        print(request)
        print(request.POST)
        print(request.FILES)
        next = request.GET.get('next', 'configfiles:view_files')
        print(next)
        return redirect(next)

class ConfigFilesFile(LoginRequiredMixin, View):
    def get(self, request, pk):

        mode = request.GET.get('mode', None)
        if mode is None:
            mode = 'view'

        file = File.objects.filter(id=pk)

        context = {
            'mode': mode,
            'items': file, 
            'view_url': 'configfiles:view_file',
            'delete_url': 'configfiles:delete_file'   
        }
        return render(request, 'configfiles/view_location.html', context)

@login_required(login_url='login')
def upload_file(request):
    pass

@login_required(login_url='login') 
def get_projects(request):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    projects = ConfigFile.objects.filter(user=request.user)
        
    context = {
        'items': projects,
        'view_url': 'configfiles:view_project',
        'delete_url': 'configfiles:delete_project',
        'col1_header': 'Name',
        'col2_header': '',
        'col3_header': '',
        'col4_header': '',
        'col5_header': '',
        'col6_header': '',
        

    }
    return render(request, 'configfiles\partials\list.html', context)


@login_required(login_url='login')
def create_project(request):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    print(request.POST)
    project_name = request.POST.get('project_name', None)
    if project_name != None:
        project = ConfigFile(name=project_name, user=request.user)
        project.save()
    
     #return render(request, 'configfiles/partials/location_list.html', context)
    return HttpResponse(status=201, headers={'HX-Trigger': 'projectListChanged'})

@login_required(login_url='login')  
def delete_project(request,pk):
    
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    project = ConfigFile.objects.get(id=pk)
    project.delete()

    #return render(request, 'configfiles/partials/location_list.html', context)
    return HttpResponse(status=204, headers={'HX-Trigger': 'projectListChanged'})

@login_required(login_url='login') 
def get_project_files(request, project_id):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    project = ConfigFile.objects.get(id=project_id)
    files = File.objects.filter(config=project)
    context = {
        'items': files,
        'project': project,
        'project_id': project.id,
        'view_file': 'configfiles:view_file',
        'edit_file': 'configfiles:edit_file',
        'delete_file': 'configfiles:delete_file',
        'next': request.GET.get('next', None),
        'view_url': 'configfiles:view_location',
        'delete_url': 'configfiles:delete_location',
        'col1_header': 'Name',
        'col2_header': 'Location',
        'col3_header': 'Environment',
        'col4_header': '',
        'col5_header': '',
        'col6_header': '',
    }
    return render(request, 'configfiles/partials/list.html', context)


@login_required(login_url='login') 
def get_locations(request):
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    locations = Location.objects.filter(user=request.user)
        
    context = {
        'items': locations,
        'view_url': 'configfiles:view_location',
        'delete_url': 'configfiles:delete_location',
        'col1_header': 'Name',
        'col2_header': '',
        'col3_header': '',
        'col4_header': '',
        'col5_header': '',
        'col6_header': '',
    }
    return render(request, 'configfiles\partials\list.html', context)

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
        'items': files,
        'location': location,
        'location_id': location.id,
        'view_file': 'configfiles:view_file',
        'edit_file': 'configfiles:edit_file',
        'delete_file': 'configfiles:delete_file',
        'next': request.GET.get('next', None),
        'view_url': 'configfiles:view_file',
        'delete_url': 'configfiles:delete_file',
        'col1_header': 'Name',
        'col2_header': 'Location',
        'col3_header': 'Environment',
        'col4_header': '',
        'col5_header': '',
        'col6_header': '',

    }
    return render(request, 'configfiles/partials/list.html', context)

@login_required(login_url='login')  
def delete_file(request, location_id, pk):
    
    if request.htmx == False:
        return Http404
    
    if request.user == None:
        return Http404
    
    
    return HttpResponse(status=204, headers={'HX-Trigger': 'fileListChanged'})
