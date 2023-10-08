from django.forms import ModelForm
from django import forms

from .models import Location, File, ConfigFile

class LocationModelForm(ModelForm):
    class Meta:
        model = Location
        fields = [ 'name' ]

    def __init__(self, *args, **kwargs):
        
        super(LocationModelForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ConfigFileModelForm(ModelForm):
    class Meta:
        model = ConfigFile
        fields = [ 'name' ]

    def __init__(self, *args, **kwargs):
        
        super(ConfigFileModelForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
