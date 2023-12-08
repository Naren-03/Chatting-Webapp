from django.shortcuts import render

# Create your views here.

# rooms = [
#     {'id':1,'name':'Learn Python'},
#     {'id':2,'name':'Learn Java'},
#     {'id':3,'name':'Learn CPP'},
# ]

def home(request):
    params = {'rooms':rooms}
    # print(params)
    return render(request,'app/home.html',params)

def room(request,pk):
    var = None
    for i in rooms:
        if i['id'] == int(pk):
            var = i
    
    params = {'val':var}
    return render(request,'app/room.html',params)

