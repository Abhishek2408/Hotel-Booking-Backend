from . import views
from django.urls import path

urlpatterns = [
    path("",views.index, name="HotelHome"),
    path("hotels/",views.hotels, name="hotels"),
    path("hotelview/<int:myid>",views.hotelview, name="hotelview"),
    path("search/",views.search, name="search"),
    path("checkout/",views.checkout, name="checkout"),
    path("contact/",views.contact, name="contact"),
    path("about/",views.about, name="about"),
]