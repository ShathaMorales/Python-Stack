from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('wall', views.wall),
    path('message', views.message),
    path('comment/<int:id>', views.comment),
    path('delete/<int:id>', views.delete),
    path('logout', views.logout),
]
