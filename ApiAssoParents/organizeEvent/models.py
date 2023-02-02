from django.db import models

# Create your models here.

class ToDo(models.Model):

    description = models.TextField(default= "Description par defaut")
    statut = models.IntegerField(default = 0)
    informations = models.TextField(default="Informations par defaut")
    orgaId = models.IntegerField(blank = False)
    userAssigned = models.TextField(null= True, blank=True)
    dateTimeAssigned = models.DateTimeField(null = True, blank = True)

class Organisation(models.Model):

    typeEvent = models.TextField(blank = True)
    description = models.TextField(blank = True)
    lieu = models.TextField(blank = True)
    date = models.DateField(blank = True)
    toDo = models.ManyToManyField(ToDo)
    horaire = models.TextField(blank = True)
    tarifs = models.TextField(blank = True)


