from django.shortcuts import render

from .models import Message

def index(request):
    return render(request , 'index.html' , {})

def room (request,room_name):
    return render(request, 'chatroom.html',{
        'room_name':room_name
        })

