from math import ceil
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Hotel
from math import ceil

# Create your views here.
def index(request):
    return render(request,'index.html')

def hotels(request):
    # hotels = Hotel.objects.all()
    # n = len(hotels)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    allHotels = []
    cathotels = Hotel.objects.values('category','id')
    cats = {hotel['category'] for hotel in cathotels}
    for cat in cats:
        prod = Hotel.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allHotels.append([prod,range(1,nSlides),nSlides,cat])
        
    # params = {'no_of_slides':nSlides,'range':range(nSlides),'hotel': hotels}
    # allHotels = [[hotels,range(1,nSlides),nSlides ],
    #              [hotels,range(1,nSlides),nSlides ],
    #              [hotels,range(1,nSlides),nSlides ]]
    params = {'allHotels':allHotels}
    return render(request,'hotels.html',params)

def hotelview(request,myid):
    hotel = Hotel.objects.filter(id=myid)
    return render(request,'hotelview.html',{'hotel':hotel[0]})

def search(request):
    return HttpResponse("Search")

def checkout(request,id):
    return HttpResponse("checkout")

def contact(request):
    return HttpResponse("contact")

def about(request):
    return render(request,'about.html')

