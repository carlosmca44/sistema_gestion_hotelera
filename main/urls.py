from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/',
         LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login/login.html'), name='logout'),

    path('reservation/new', views.createReservation, name='newReservation'),
    path('reservation/delete/<int:reservationId>/',
         views.deleteReservation, name="deleteReservation"),
    path('reservation/edit/<int:reservationId>',
         views.editReservation, name='editReservation'),
    
    
    path('csuggestion/edit/<int:csuggestionId>',
         views.editCSuggestion, name='editCSuggestion'),
    path('csuggestion/delete/<int:csuggestionId>/',
         views.deleteCSuggestion, name="deleteCSuggestion"),
    
    path('csuggestion/response/edit/<int:csuggestionId>/',
         views.editReponseCSuggestion, name='editResponseCSuggestion'),
    
    
    
    
]
