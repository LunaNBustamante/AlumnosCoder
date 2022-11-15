from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length = 50) ##String
    camada = models.IntegerField() ##Numeros

class Estudiantes(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.EmailField()
    profesion = models.CharField(max_length= 50)

class Entregable(models.Model):
    nombre = models.CharField(max_length= 50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

class Pepito(models.Model):
    ejemplo = models.CharField(max_length= 50)

##Cada vez que creemos una nueva clase debemos correr make manage.py make migrations y migrate para que se guarde la base de datos



##Esto es para migrar la base de datos 

cursos = Curso.objects.all()