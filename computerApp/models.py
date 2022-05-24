from datetime import datetime 
from django.db import models

#create your models here.
class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintain and connect servers')),
        
    )
    id = models.AutoField(
        primary_key = True,
        editable=False)
    nom=models.CharField(
        max_length=6)
    maintenaceDate = models.DateField(
        default = datetime.now())
    mach = models.CharField(
        max_length=32, choices=TYPE, default='PC')

    def __str__(self):
        return str(self.id) + " ===> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom
class Personnel(models.Model):
    num_secu= models.CharField(
        primary_key= True,
        editable=True,
        max_length=13
    )
    nom=models.CharField(
        max_length=30
    )
    prenom=models.CharField(
        max_length=10
    )
    

    def __str__(self):
        return str(self.num_secu) + " ===> " + self.nom + " " + self.prenom
