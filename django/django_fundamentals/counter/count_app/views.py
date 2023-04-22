from django.shortcuts import render, redirect


def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    context = {
        'counter': request.session['counter']
    }
    return render(request, 'index.html', context)


def destroy(request):
    del request.session['counter']
    return redirect('/')


def increment(request):
    request.session['counter'] += 1
    return redirect('/')
