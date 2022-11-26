from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/',
         LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login/login.html'), name='logout'),
    path('signin/', views.auth_signin, name='signin'),
    path('reservations/', views.reservations, name='reservations'),
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
         views.deleteCSuggestion, name="deleteCSuggestion"),
    path('csuggestion/response/<int:csuggestionId>/',
         views.askCSuggestion, name='askcsuggestion'),
    path('csuggestion/response/edit/<int:csuggestionId>/',
         views.editReponseCSuggestion, name='editResponseCSuggestion')
]
