from django.conf import settings as django_settings

from users.models import User, UserSettings

def settings(request):
    return {
        'settings': django_settings,
    }

def confirm_delete(request):
    try:
            
        user = User.objects.get(id=request.user.id)
        return {
            'confirm_delete': user.usersettings.confirm_delete,
        }
    except:
        return { 'confirm_delete': ''}
    