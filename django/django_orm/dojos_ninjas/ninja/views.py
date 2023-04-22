from django.shortcuts import render, redirect
from . models import *


def index(request):
    context = {
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)


def dojo(request):
    Dojo.objects.create(
        name=request.POST['dojo_name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')


def ninja(request):
    Ninja.objects.create(first_name=request.POST['ninja_first_name'],
                        last_name=request.POST['ninja_last_name'], dojo=Dojo.objects.get(id=request.POST['dojo']))
    return redirect('/')
