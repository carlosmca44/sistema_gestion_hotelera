from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Reservacion)
admin.site.register(Habitacion)
admin.site.register(Reclamacion)
admin.site.register(Hospedaje)