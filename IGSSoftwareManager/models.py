from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    departament = models.ForeignKey('Departament',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Departament(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
