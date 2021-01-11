from .views import RoomView, CreateRoomView, GetRoom, JoinRoom
from django.urls import path

urlpatterns = [
    path('room',RoomView.as_view()),
    path('create-room',CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
]