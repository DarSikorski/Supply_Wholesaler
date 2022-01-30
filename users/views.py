import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from warehouse.models import Customer
from .forms import RegisterUserForm
from django.core.mail import send_mail


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('warehouse')
		else:
			messages.success(request, ("Złe dane, ponów próbe..."))	
			return redirect('login')	


	else:
		return render(request, 'warehouse/login.html', {})

def logout_user(request):
	logout(request)
	return redirect('warehouse')


def register_user(request):
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            userr = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            Customer.objects.create(user=userr,name = username, email=email)
            
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Pomyślnie zarejestrowano!"))
            send_mail(
                'Witamy w Hurtowni Mojżesz',
                'Witaj '+form.cleaned_data['first_name']+' '+form.cleaned_data['last_name']+'\n'
                'Dziękujemy za założenie konta: \n'+
                'Email: '+ email +'\n'
                'Nazwa użytkownika: '+username +'\n',
                'hurtowniahydraulicznamojzesz@yahoo.com',
                ['hurtowniahydraulicznamojzesz@yahoo.com'],
                fail_silently=False,
                ) 
            return redirect('warehouse')
           
    return render(request, 'warehouse/register.html',{
        'form':form,
        })
