from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout

#------------------registering by UserCreationForm-------------------------
# from django.contrib.auth.forms import UserCreationForm
# from django.views import generic
# from django.urls import reverse_lazy

# class UserCreateView(generic.CreateView):
# 	form_class =UserCreationForm
# 	template_name ='signup.html'
# 	success_url =reverse_lazy('login')
#---------------------------------------------------------------------------

def register_user(request):
	if request.method == "POST":
		username =request.POST['username']
		password =request.POST['password']
		user =User.objects.create_user(username=username, password=password)
		user.save()
		return redirect('login')
		
	ctx ={}
	return render(request, 'signup.html',ctx)

def login_user(request):
	if request.method == "POST":
		username =request.POST['username']
		password =request.POST['password']
		user =authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect('home')
		
	ctx ={}
	return render(request, 'registration/login.html',ctx)	

def logout_user(request):
	logout(request)
	return redirect('home')
	