from django.contrib.auth import (
	login, 
	logout,
	authenticate,
	get_user_model,

)
from .forms import UserLoginForm, UserRegistrationForm
from django.shortcuts import render, redirect


def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)

		return redirect('/')  
	context = {'form': form }

	return render(request, "accounts/login.htm", context)


def signup_view(request):
	next = request.GET.get('next')
	form = UserRegistrationForm(request.POST or None)
	#form = UserRegistrationForm(request.POST)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect('/')


	return render(request, 'accounts/signup.htm', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('/')