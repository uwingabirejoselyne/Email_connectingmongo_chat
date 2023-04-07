from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('invitation/<int:id>',views.send_invitation,name='invitation'),
    path('searchuser',views.searchUser,name='searchuser'),
    path('friend',views.view_invitation,name='friend'),
    ]