from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCustomerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('mapping:homepage')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mapping:homepage') 
        else:
            messages.info(request, 'Identifiant ou mot de passe incorrect')
    
    #formular = AuthenticationForm()          
    context = {
        'page':page,
        #'form':formular,
    }

    return render(request, 'accounts/login_signup.html', context)

def signupUser(request):
    if request.method == 'POST':
        formular = UserCustomerForm(request.POST)
        if formular.is_valid():
            user = formular.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user) # Login user after creation
            return redirect('mapping:homepage') # Homepage is the name given to the home url
        else:
            messages.error(request, 'Une erreur durant la création')
    
    else:
        formular = UserCustomerForm()

    context = {
        'form': formular,
        }

    return render(request, 'accounts/login_signup.html', context)

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('mapping:homepage')

    return render(request, 'accounts/logout.html')
