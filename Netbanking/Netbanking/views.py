from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def hello_world (request) :
    messg = "<h1>Hello World !!!</h1>"
    return HttpResponse( messg )

def index_page(request):
    return HttpResponse("this is my django project")

def home_view(request):
# logic of view will be implemented here
    return render(request, "home.html")

class AboutUs(View):
    def get(self, request):
        return HttpResponse('We provide all solutions.')