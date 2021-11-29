from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
import string

from api.models import Room

# Create your views here.
# def index(request):
#   if request.method == 'POST':
#     roomname = 'RandomRoom' if request.POST.get('roomname') == "" else request.POST.get('roomname')
#     username = 'Anonymous' if request.POST.get('username') == "" else request.POST.get('username')
#     user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
#     return HttpResponseRedirect(reverse('rooms',args=[roomname,username,user_id]))
#   return render(request, 'chatroom/index.html')

def rooms(request,roomname):
  room = Room.objects.get(id=int(roomname))
  roomname = room.title
  user = request.user.first_name + ' ' + request.user.last_name
  return render(request, 'chatroom.html', {
    'roomname': roomname,
    'user': user,
    'user_id': request.user.id,
    'auth': request.user
  })
