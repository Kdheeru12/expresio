# chat_app/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('<str:roomname>/', views.rooms, name='rooms'),
]