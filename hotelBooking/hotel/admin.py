from django.contrib import admin

# Register your models here.
from .models import Contact, Hotel
admin.site.register(Hotel)
admin.site.register(Contact)
