from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')


def validate_login(request):
    user = User.objects.get(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
        print("password match")
    else:
        print("failed password")


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=first_name,
                            last_name=last_name, email=email, password=pw_hash)
        newUser = User.objects.last().first_name
        request.session['newUser'] = newUser
    return redirect('/success')


def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['newUser'] = logged_user.first_name
            return redirect('/success')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('/')
    else:
        messages.error(request, 'Invalid Credentials!')
        return redirect('/')


def success(request):
    return render(request, 'success.html')


def logout(request):
    request.session.delete()
    return redirect('/')
