from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def hotels(request):
    return HttpResponse("Hotels all")

def hotelview(request):
    return HttpResponse("Hotelview")

def search(request):
    return HttpResponse("Search")

def checkout(request):
    return HttpResponse("checkout")

def contact(request):
    return HttpResponse("contact")

def about(request):
    return HttpResponse("About")

