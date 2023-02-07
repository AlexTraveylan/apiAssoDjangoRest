from django.db import models

from organizeEvent.validators import *

# Create your models here.

class ToDo(models.Model):

    description = models.TextField(default= "Description par defaut")
    statut = models.IntegerField(default = 0)
    informations = models.TextField(default="Informations par defaut")
    orgaId = models.IntegerField(blank = False)
    userAssigned = models.TextField(null= True, blank=True, validators=[validate_username])
    dateTimeAssigned = models.DateTimeField(null = True, blank = True)

class Organisation(models.Model):

    password = models.TextField(unique = True, validators=[validate_password])
    typeEvent = models.TextField(blank = True)
    description = models.TextField(blank = True)
    lieu = models.TextField(blank = True)
    date = models.DateField(blank = True)
    toDo = models.ManyToManyField(ToDo)
    horaire = models.TextField(blank = True)
    tarifs = models.TextField(blank = True)

class Comptabilite(models.Model):

    date = models.DateField(null= False, blank = False)
    source = models.TextField(blank = True)
    label = models.TextField(blank = True)
    amount = models.IntegerField(blank = False, null = False)
    paiementType = models.TextField(blank = False)
    isPositive = models.BooleanField(blank = False)
    note = models.TextField(blank = True, null = True)
    requestToken = models.TextField(blank = True, null = True)

