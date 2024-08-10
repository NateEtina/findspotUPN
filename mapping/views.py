from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Building, Bureau, Local, Office, Space

def index(request):
    page = 'home'
    search_term = request.GET.get('searchbar')
    buildings = Building.objects.all()
    bureaux = Bureau.objects.all()
    offices = Office.objects.all()
    locals_ = Local.objects.all()
    spaces = Space.objects.all()

    if search_term :
        search_result  = Building.objects.filter(
            Q(name__icontains=search_term)
        )
    else:
        search_result = []
   
    #maps_center = Space.objects.get(name='centre du campus')

    context = {
        'page':page,
        'buildings':buildings,
        'bureaux':bureaux,
        'offices':offices,
        'locals':locals_,
        'spaces':spaces,
        'search_result':search_result,
        'search_term':search_term,
        #'center':maps_center,
    }
    return render(request, 'mapping/home.html', context)

def showBuilding(request):
    page = 'building'
    buildings = Building.objects.all()
    context = {'buildings':buildings,'page':page,}

    return render(request, 'mapping/home.html', context)

def showBureau(request):
    page = 'bureau'
    bureaux = Bureau.objects.all()
    context = {'page':page,'bureaux':bureaux}

    return render(request, 'mapping/home.html', context)

def showLocal(request):
    page = 'local'
    locals_ = Local.objects.all()
    context = {'page':page,'locals':locals_}

    return render(request, 'mapping/home.html', context)

def showSpace(request):
    page = 'space'
    spaces = Space.objects.all()
    context = {'page':page,'spaces':spaces}

    return render(request, 'mapping/home.html', context)

@login_required(login_url='login')
def showInterestPoint(request):
    page = 'interestpoint'
    buildings = Building.objects.filter(interest=True)
    offices = Office.objects.filter(interest=True)
    spaces = Space.objects.filter(interest=True)

    context = {
        'page':page,
        'buldings':buildings,
        'offices':offices,
        'spaces':spaces
    }

    
#def display
"""@login_required(login_url='login')
def addEvent(request):
    pass"""
