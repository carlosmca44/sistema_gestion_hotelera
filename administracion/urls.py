from django.urls import path
from .views import *

urlpatterns = [
    path('', indexA, name='indexA'),
    path('reservations/', reservations, name='reservations'),

    # Reclamaciones
    path('csuggestion/', complaintSuggestion, name='reclamaciones'),
    path('csuggestion/response/<int:csuggestionId>/', askCSuggestion, name='askcsuggestion'),

    # Usuarios
    path('users-management/', usersManagement, name='usuarios'),
    path('users-management/new/', createUser, name='createUser'),
    path('users-management/delete/<int:userId>/', deleteUser, name="deleteUser"),
    path('users-management/edit/<int:userId>', editUser, name='editUser'),
]