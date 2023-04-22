from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.display),
    path('shows/new', views.show_form),
    path('shows/create', views.create),
    path('shows/<int:id>', views.preview),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/update', views.update),
    path('shows/<int:id>/delete', views.delete),
]
