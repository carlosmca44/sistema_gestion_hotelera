from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Habitacion(models.Model):
    roomNumber = models.IntegerField(primary_key=True)
    dispo = models.BooleanField(default=True)

    def __str__(self):
        return self.roomNumber.__str__()


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


class Reservacion(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    entry_date = models.DateField()
    out_date = models.DateField()
    roomNumber = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class QSugerencias(models.Model):
    name = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
    roomNumber = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    info = models.CharField(max_length=500)
    doneResponse = models.BooleanField(default=False)
    response = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name.__str__()
