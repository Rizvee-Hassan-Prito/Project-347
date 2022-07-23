from django.shortcuts import render,redirect
from .models import Account
from django.contrib.auth import login, authenticate, logout
from app.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

def homepage(request):
    return render(request, 'home.html')

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return render(request, 'home.html')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return render(request, 'home.html')

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return render(request, 'home.html')

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "login.html", context) 

def account_view(request):
    
    
    if not request.user.is_authenticated:
        return render(request, "login.html")
	
    #account = Account.objects.get(pk=request.user.id)
    
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            context['account_form'] = form
            context['success_message'] = 'Your account is updated.'
            return render(request, "account.html", context)
        else:
            context['account_form'] = form
            return render(request, "account.html", context)
    else:
        form = AccountUpdateForm(
			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)
        context['account_form'] = form
        return render(request, "account.html", context)

def delete(request):
    if request.POST:
        user = request.user
        if user.is_authenticated: 
            request.user.delete()
        return render(request, "login.html")  
    else:
        return render(request, "delete.html")