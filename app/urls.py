from django.urls import path,include
from . import views 



urlpatterns = [
    path('login',views.loginpage,name='login'),
    path('register',views.registerpage,name='register'),
    path('logout',views.logoutpage,name='logout'),
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room',views.create_room,name='create-room'),
    path('update-room/<str:pk>/',views.update_room,name='update-room'),
    path('user-profile/<str:pk>/',views.userprofile,name='user-profile'),
    path('delete-room/<str:pk>/',views.delete_room,name='delete-room'),
    path('delete-message/<str:pk>/',views.delete_msg,name='delete-message'),
    path('update-user/',views.updateUser,name='update-user'),
    path('topics/',views.topicsPage,name='topics'),
    path('activity/',views.activityPage,name='activity'),
]
