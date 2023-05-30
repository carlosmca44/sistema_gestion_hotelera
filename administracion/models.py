from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserProfile(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, max_length=20)
    password = models.CharField(max_length=15, null=True)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.username.__str__()


class User(AbstractUser):
    category = models.CharField(max_length=20)

class Habitacion(models.Model):
    roomNumber = models.IntegerField()
    dispo = models.BooleanField(default=True)

    def __str__(self):
        return self.roomNumber.__str__()


class Reservacion(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    entry_date = models.DateField()
    out_date = models.DateField()
    habitaciones = models.ManyToManyField(Habitacion, related_name='reservaciones')
    ejecutada = models.BooleanField(default=False)
    cancelada = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.username + ' - ' + self.entry_date.__str__()


class Reclamacion(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    info = models.CharField(max_length=500)
    doneResponse = models.BooleanField(default=False)
    response = models.CharField(max_length=500, default='')

    def __str__(self):
        return 'reclamacion' + self.habitacion.__str__()


class Hospedaje(models.Model): 
    reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE, related_name='hospedajes')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.reservacion.__str__() + ' - ' + self.habitacion.__str__()
