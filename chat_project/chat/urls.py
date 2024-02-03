from django.urls import path
from .views import MessageList, UserList

urlpatterns = [
    path('messages/', MessageList.as_view(), name='message-list'),
    path('users/', UserList.as_view(), name='user-list'),
]
