from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_login, name='login'),
    path('signin/', views.auth_signin, name='signin'),
    path('home/', views.home, name='home'),
]
