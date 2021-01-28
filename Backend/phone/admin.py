from django.contrib import admin
from .models import Persons



class PersonsAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone_number','email','rel']
    

admin.site.register(Persons, PersonsAdmin)