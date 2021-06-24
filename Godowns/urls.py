from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
path('', views.home,name='home'),
path('Godown_details/', views.Godown_details, name='Godown_details'),
path('Storage_details/', views.Storage_details, name='Storage_details'),
path('Registration/', views.Registration, name='Registration'),
path('Login/', views.Login, name='Login'),
path('Logout/', views.Logout, name='Logout'),
path('Customer/', views.Customer, name='Customer'),
]