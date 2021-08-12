# views.py
from django.shortcuts import render,redirect,get_object_or_404
from user.models import *
from chat.models import *

def index(request,id):
    contact = User.objects.get(pk=id)
    user_pk = request.session.get('user')
    if not user_pk :
        return redirect('/login')
    elif user_pk:
        user = User.objects.get(user_pk)
        room_name = str(user)+str(contact)
        room = Room()
        room.room_name = room_name
        room.save()
        return redirect('/chat/'+room.room_name)
    return render(request, 'index.html', {})

def room(request,id, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })