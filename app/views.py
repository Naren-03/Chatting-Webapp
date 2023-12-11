from django.shortcuts import render,redirect
from .models import Room,Topic
from django.http import HttpResponse
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# rooms = [
#     {'id':1,'name':'Learn Python'},
#     {'id':2,'name':'Learn Java'},
#     {'id':3,'name':'Learn CPP'},
# ]


def loginpage(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username not exist')

        auth_user = authenticate(request,username=username,password=password)

        if auth_user is not None:
            login(request,auth_user)
            return redirect('home')       
        else:
            messages.info(request,'Username OR Password not exist')

    return render(request,'app/login_register.html',context)

def logoutpage(request):
    logout(request)
    return redirect('home')


def home(request):

    # Filtering the data 
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
                            Q(topic__name__icontains=q) | 
                            # Q(name__icontains = q) |
                            Q(description__icontains = q) |
                            Q(host__username__icontains = q) 
                            )

    topic = Topic.objects.all() 
    room_count = rooms.count()
    params = {'rooms':rooms,'topics':topic,'room_count':room_count}
    # print(params)
    return render(request,'app/home.html',params)

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    params = {'room':rooms}
    return render(request,'app/room.html',params)


@login_required(login_url='login')
def create_room(request):

    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST) #passing data to Form to store in Database
        # print(request.POST) Show data in Dict form
        if form.is_valid():
            form.save()
            return redirect('home')
    params  = {'form':form}
    return render(request,'app/room_form.html',params)

@login_required(login_url='login')
def update_room(request,pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not Allowed')
    
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    params = {'form':form}
    return render(request,'app/room_form.html',params)


@login_required(login_url='login')
def delete_room(request,pk):
    room = Room.objects.get(id = pk)

    if request.user != room.host:
        return HttpResponse('You are not Allowed')

    if request.method == "POST":
        room.delete()
        return redirect('home')

    params = {'obj':room}
    return render(request,'app/delete_room.html',params)