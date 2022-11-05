from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Departament(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class EmergencyContact(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    adress = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    emegency = models.ForeignKey(EmergencyContact, on_delete=models.SET_NULL,
                                 null=True, blank=True)

    def full_name(self):
        return self.name + ' ' + self.surname.upper()

    def __str__(self):
        return self.name
