from django.shortcuts import render, redirect
import random


def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        print(request.session['number'])
    return render(request, 'index.html')


def guess(request):
    print(request.session['number'])
    request.session['test'] = request.POST['option']
    if int(request.session['test']) == int(request.session['number']):
        request.session['status'] = 'correct'
    elif int(request.session['test']) > int(request.session['number']):
        request.session['status'] = 'higher'
    elif int(request.session['test']) < int(request.session['number']):
        request.session['status'] = 'lower'
    return redirect('/')


def back(request):
    return redirect('/')


def clear(request):
    request.session.clear()
    return redirect('/')
