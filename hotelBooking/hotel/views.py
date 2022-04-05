from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Hotel
from math import ceil

# Create your views here.
def index(request):
    return render(request,'index.html')

def hotels(request):
    hotels = Hotel.objects.all()
    print(hotels)
    n = len(hotels)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides,'range':range(nSlides),'hotel': hotels}
    return render(request,'hotels.html',params)

def hotelview(request):
    return HttpResponse("Hotelview")

def search(request):
    return HttpResponse("Search")

def checkout(request):
    return HttpResponse("checkout")

def contact(request):
    return HttpResponse("contact")

def about(request):
    return render(request,'about.html')

