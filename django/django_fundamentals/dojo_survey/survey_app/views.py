from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def result(request):
    first_name_from_form = request.POST['first_name']
    last_name_from_form = request.POST['last_name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    submit_from_form = request.POST['submit']

    context = {
        'first_name': first_name_from_form,
        'last_name': last_name_from_form,
        'location': location_from_form,
        'language': language_from_form,
        'comment': comment_from_form,
    }
    return render(request, 'result.html', context)


def back(request):
    back_from_form = request.POST['back']
    if back_from_form == 'yes':
        return redirect('/')
