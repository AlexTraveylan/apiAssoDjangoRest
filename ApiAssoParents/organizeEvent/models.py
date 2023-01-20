from django.db import models

# Create your models here.

class ToDo(models.Model):

    description = models.TextField(blank = True)
    isChecked = models.BooleanField(default = False)
    informations = models.TextField(default="Informations par defaut")
    orgaId = models.IntegerField(blank = False)

class Organisation(models.Model):

    typeEvent = models.TextField(blank = True)
    description = models.TextField(blank = True)
    lieu = models.TextField(blank = True)
    date = models.TextField(blank = True)
    toDo = models.ManyToManyField(ToDo)
    horaire = models.TextField(blank = True)
    tarifs = models.TextField(blank = True)


