from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views import View
# Create your views here.

class index(View):
    def get(self, request):
        for item in request:
            print(item)
        return render(request, "index.html")