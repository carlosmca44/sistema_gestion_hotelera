from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_login, name='login'),
    path('signin/', views.auth_signin, name='signin'),
    path('home/', views.home, name='home'),
    path('reservation/new', views.createReservation, name='newReservation'),
    path('reservation/delete/<int:reservationId>/',
         views.deleteReservation, name="deleteReservation"),
    path('reservation/edit/<int:reservationId>',
         views.editReservation, name='editReservation'),
    path('csuggestion/', views.complaintSuggestion, name='csuggestions'),
    path('csuggestion/new', views.createCSuggestion, name='newCSuggestion'),
    path('csuggestion/edit/<int:csuggestionId>',
         views.editCSuggestion, name='editCSuggestion'),
    path('csuggestion/delete/<int:csuggestionId>/',
         views.deleteReservation, name="deleteCSuggestion"),
    path('reservation/delete/<int:reservationId>/',
         views.deleteReservation, name="deleteReservation"),
]
