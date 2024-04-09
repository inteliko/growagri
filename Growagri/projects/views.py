
from django.shortcuts import render
from django.http import HttpResponse
from farm.models import Farm

def home(request):
    farms = Farm.objects.all().filter(is_available=True)

    context ={
        'farms': farms,
    }

    return render(request, 'home.html', context)



def login(request):
    return render(request, 'account/login.html')

def signup(request):
    return render(request, 'account/signup.html')

def about(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'legal/faq.html')


