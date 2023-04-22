from django.shortcuts import render, redirect
import random
import datetime


def index(request):
    if 'earnings' not in request.session:
        request.session['earnings'] = 0
    if 'textarea' not in request.session:
        request.session['textarea'] = []
    return render(request, 'index.html')


def process(request):
    arr = ['farm', 'cave', 'house']
    x = request.POST['which_form']
    worth = 'green'
    time = datetime.datetime.now().strftime('%B,%d %Y %I:%M %p')
    if x in arr:
        num = random.randint(10, 20)
        act = f'You entered a {x} and earned {num} gold. {time}'
    else:
        num = random.randint(-50, 50)
        if num >= 0:
            act = f'You entered a {x} and earned {num} gold. {time}'
        else:
            act = f'You failed a {x} and lost {abs(num)} gold. Ouch {time}'
            worth = 'red'

    request.session['earnings'] += num
    request.session['textarea'].append({'name': act, 'color': worth})
    return redirect('/')


def clear(request):
    request.session.clear()
    return redirect('/')
