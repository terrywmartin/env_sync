from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import User, UserSettings

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        
        super(RegisterUserForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
  
class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email' ]

    def __init__(self, *args, **kwargs):
        
        super(UserModelForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
class UserSettingsForm(ModelForm):
    class Meta:
        model = UserSettings
        fields = [ 'confirm_delete' ]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['confirm_delete'].label = 'Confirm before delete'
        for name, field in self.fields.items():
            print(name)
            field.widget.attrs.update({'class': 'form-check-input'})
