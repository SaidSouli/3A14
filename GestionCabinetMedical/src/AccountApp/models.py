from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator , MaxLengthValidator , RegexValidator

class User(AbstractUser):
    pass

class Doctor (User):
    license_number = models.CharField(max_length=6,unique=True,blank=False, validators=[MinLengthValidator])
    phone = models.CharField(max_length=8,unique=True, validators=[RegexValidator])
    specialties = models.ManyToManyField('Specialty',related_name='doctors')
class Patient(User):
    national_id = models.CharField(max_length=6,unique=True,blank=False)
    phone = models.CharField(max_length=8,unique=True)
    birth_date = models.DateField()
class Specialty(models.Model):
    name = models.CharField(max_length=50)
    doctors = models.ManyToManyField(Doctor)
