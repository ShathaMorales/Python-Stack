from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')


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
        newUser = User.objects.last().id
        request.session['newUser'] = newUser
    return redirect('/success')


def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['newUser'] = logged_user.id
            return redirect('/wall')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('/')
    else:
        messages.error(request, 'Invalid Credentials!')
        return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')


def success(request):
    context = {
        'User': User.objects.get(id=request.session['newUser']),
    }
    return render(request, 'success.html', context)


def wall(request):
    if 'newUser' not in request.session:
        return redirect('/')
    context = {
        'User': User.objects.get(id=request.session['newUser']),
        'all_messages': Message.objects.order_by('-created_at')
    }
    return render(request, "wall.html", context)


def message(request):
    message = request.POST['textarea']
    logged_user = User.objects.get(id=request.session['newUser'])
    Message.objects.create(message=message, user=logged_user)
    return redirect('/wall')


def comment(request, id):
    comment = request.POST['comment']
    logged_user = User.objects.get(id=request.session['newUser'])
    message = Message.objects.get(id=id)
    Comment.objects.create(
        comment=comment, user=logged_user, message=message)
    return redirect('/wall')


def delete(request, id):
    message = Message.objects.get(id=id)
    message.delete()
    return redirect('/wall')
