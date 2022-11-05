from django.contrib import admin

from .models import EmergencyContact, Employee, Departament

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmergencyContact)
admin.site.register(Departament)