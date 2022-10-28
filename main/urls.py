from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_login, name='login'),
    path('home/', views.home, name='home')
]
