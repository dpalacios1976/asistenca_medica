from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES =(
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otro'),
    )

    TYPE_CHOICES =(
        ('C','Cédula'),
        ('P','Pasaporte'),
        ('V','Visa'),
        ('R','Carné Refugiado'),
    )

    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=120,unique=True)
    names = models.CharField('Nombres', max_length=80,blank=True)
    surnames = models.CharField('Apellidos', max_length=80,blank=True)
    gender = models.CharField('Genero', max_length=1,choices=GENDER_CHOICES) 
    id_type = models.CharField('Tipo Id',max_length=1,choices=TYPE_CHOICES)
    id_number = models.CharField('Número de Indentificación', max_length=10,unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username
    def get_full_name(self):
        return self.names + ' ' + self.surnames
    
