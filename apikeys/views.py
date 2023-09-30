from django.shortcuts import render

from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class CreateAPIKey(LoginRequiredMixin,View):
    def get(self):

        context = {}
        return

class DeleteAPIKey(LoginRequiredMixin,View):
    def delete(self, pk):

        return