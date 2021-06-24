from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.db.models import When, Case, F, IntegerField
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, 'Godowns/Homepage.html')


def Godown_details(request):
	#return render(request, 'Godowns/Godown.html')
	if request.GET.get('type'):
		food_filter = request.GET.get('type')
		godown_data = Godown.objects.filter(Food_Type = food_filter)

	#if request.GET.get('city'):
	#	city_filter = request.GET.get('city')
	#	godown_data = Godown.objects.filter(City = city_filter)
	else:
		godown_data = Godown.objects.all()

	return render(request, 'Godowns/Godown.html', {'godown_data': godown_data} )

def Storage_details(request):
	#return render(request, 'Godowns/Storage.html')
	if request.GET.get('city_name'):
		city_filter = request.GET.get('city_name')
		storage_data = Storage.objects.filter(City = city_filter)
	else:
		storage_data = Storage.objects.all()

	return render(request, 'Godowns/Storage.html', {'storage_data': storage_data} )


def Registration(request):
	if request.method == 'POST':
		First_Name = request.POST['F']
		Last_Name = request.POST['L']
		User_Name = request.POST['U']
		Email = request.POST['E']
		Password = request.POST['P']
		user = User.objects.create_user(first_name = First_Name ,last_name = Last_Name ,username = User_Name ,  email = Email,password = Password ,)
		user.save()
		return render(request, 'Godowns/Login.html')
	else:
		return render(request, 'Godowns/Registration.html')


	

def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'Godowns/Customer.html')
		else:
			messages.error(request,"Wrong Credential")
			return render(request, 'Godowns/Login.html')
	else:
		return render(request, 'Godowns/Login.html')
	
def Logout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return render(request, 'Godowns/Login.html')

def Customer(request):
	return render(request, 'Godowns/Customer.html')