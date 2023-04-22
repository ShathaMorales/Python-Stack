from django.shortcuts import render, redirect
from . models import *


def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def add_book(request):
    Book.objects.create(
        title=request.POST['title'], desc=request.POST['description'])
    return redirect('/')


def book_preview(request, id):
    context = {
        'booknum': Book.objects.get(id=int(id)),
        'all_authors': Author.objects.all()
    }
    return render(request, 'book_preview.html', context)


def create_author(request, id):
    authornum = Author.objects.get(id=request.POST['author'])
    book = Book.objects.get(id=int(id))
    book.authors.add(authornum)
    return redirect('/books/'+str(id))


def index2(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)


def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')


def author_preview(request, id):
    context = {
        'authornum': Author.objects.get(id=int(id)),
        'all_books': Book.objects.all()
    }
    return render(request, 'author_preview.html', context)


def create_book(request, id):
    booknum = Book.objects.get(id=request.POST['book'])
    author = Author.objects.get(id=int(id))
    author.books.add(booknum)
    return redirect('/authors/'+str(id))
