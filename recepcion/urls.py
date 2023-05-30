from django.urls import path
from .views import *

urlpatterns = [
    path('', indexR, name='indexR'),
    path('reservations-r/', reservationsR, name='reservationsR'),
    path('csuggestion-r/', complaintSuggestionR, name='reclamacionesR'),
    path('csuggestion-r/new', createCSuggestion, name='newCSuggestion'),
]