from django.shortcuts import render
from . models import User


def index(request):
    if request.method == 'POST':
        User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], age=request.POST['age'])

        context = {
            "all_users": User.objects.all()
        }

    return render(request, 'index.html')
