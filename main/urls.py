from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_login, name='login'),
    path('signin/', views.auth_signin, name='signin'),
    path('home/', views.home, name='home'),
    path('reservation/new', views.createReservation, name='newReservation'),
    path("deleteReservation/<int:reservationId>/",
         views.deleteReservation, name="deleteReservation"),
]
