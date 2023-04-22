from django.shortcuts import render, redirect
from . models import *


def index(request):
    return redirect('/shows')


def display(request):
    context = {
        'all_shows': Shows.objects.all()
    }
    return render(request, 'display.html', context)


def show_form(request):
    return render(request, 'show.html')


def create(request):
    Shows.objects.create(title=request.POST['title'], network=request.POST['network'],
                        release_date=request.POST['date'], description=request.POST['description'])
    return redirect('/shows/'+str(Shows.objects.last().id))


def preview(request, id):
    context = {
        'shownum': Shows.objects.get(id=int(id)),
        'all_shows': Shows.objects.all()
    }
    return render(request, 'create.html', context)


def edit(request, id):
    context = {
        'shownum': Shows.objects.get(id=int(id)),
    }
    return render(request, 'edit.html', context)


def update(request, id):
    shownum = Shows.objects.get(id=int(id))
    shownum.title = request.POST['title']
    shownum.network = request.POST['network']
    shownum.save()
    return redirect('/shows/' + str(id))


def delete(request, id):
    shownum = Shows.objects.get(id=int(id))
    shownum.delete()
    return redirect('/shows')
