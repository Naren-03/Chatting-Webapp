from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id':1,'name':'Learn Python'},
#     {'id':2,'name':'Learn Java'},
#     {'id':3,'name':'Learn CPP'},
# ]


def home(request):
    rooms = Room.objects.all()
    params = {'rooms':rooms}
    # print(params)
    return render(request,'app/home.html',params)

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    params = {'room':rooms}
    return render(request,'app/room.html',params)


def create_room(request):

    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST) #passing data to Form to store in Database
        # print(request.POST) Show data in Dict form
        form.save()
        return redirect('home')
    params  = {'form':form}
    return render(request,'app/room_form.html',params)