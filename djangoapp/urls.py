
from . import views
from django.urls import path

urlpatterns = [
  #  path('test',views.index,name='index'),
    path('invitation/<int:id>',views.send_invitation,name='invitation'),
    path('searchuser',views.searchUser,name='searchuser'),
    path('friend',views.view_invitation,name='friend'),
    path('accept/<int:id>',views.Accept_invitation,name='accept'),
    path('cancel/<int:id>',views.Cancel_invitation,name='cancel'),
    path('chat',views.ChatRoom,name='chat'),
    path('chat/<str:name>',views.individuachat,name='individuachat'),
    path('',views.Home,name='home'),
    ]