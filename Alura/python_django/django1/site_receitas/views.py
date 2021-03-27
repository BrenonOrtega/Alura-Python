from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views import View
from django.contrib.staticfiles import finders
# Create your views here.

class index(View):
    def get(self, request):
        return render(request, "index.html")