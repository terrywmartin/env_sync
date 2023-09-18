from django.shortcuts import render

from django.views import View


# Create your views here.
class CreateAPIKey(View):
    def get(self):

        context = {}
        return

class DeleteAPIKey(View):
    def delete(self, pk):

        return