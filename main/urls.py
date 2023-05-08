from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/',
         LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login/login.html'), name='logout'),

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
         views.editReponseCSuggestion, name='editResponseCSuggestion'),
    path('users-management/', views.usersManagement, name='userManagement'),
    path('users-management/new/', views.createUser, name='createUser'),
    path('users-management/delete/<int:userId>/',
         views.deleteUser, name="deleteUser"),
    path('users-management/edit/<int:userId>',
         views.editUser, name='editUser'),
]
