from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.add_book),
    path('books/<int:id>', views.book_preview),
    path('addauthor/<int:id>', views.create_author),
    path('authors', views.index2),
    path('addauthor', views.add_author),
    path('authors/<int:id>', views.author_preview),
    path('addbook/<int:id>', views.create_book),
]
