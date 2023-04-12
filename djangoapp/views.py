from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.core.mail import settings
import datetime
x = datetime.datetime.now()
current_date=x.strftime("%Y-%m-%d %H:%M:%S")

import pymongo

# Create your views here.
def index(request):
    if request.method == 'POST':
        courseId= request.POST['courseId']
        coursename = request.POST['coursename']
        email_body = 'Course ID: '+str(courseId)+'nCourse Name: '+coursename

        email = EmailMessage(
        'course form',
        email_body,
        settings.EMAIL_HOST_USER,
        ['uwingajoselyne@gmail.com'],
       
        )
        email.fail_silently = False
        email.send()
        print(email)
    return render(request,'index.html')
# client = pymongo.MongoClient('mongodb://127.0.0.1:27017/myBrandDb')
client = pymongo.MongoClient('mongodb+srv://joselyne:12345@myapi.19iwnvv.mongodb.net/?retryWrites=true&w=majority')
dbname = client['jose']

#Define Collection
collection = dbname['student']

doc={
    "studentId": "wetryui",
    "first_name" : "srdtfg",
    "last_name" : "Josew123",
    "email" : "uwingajoselyne@gmail.com"
}

collection.insert_one(doc)

mascot_details = collection.find({})

@login_required
def send_invitation(request,id):
    data = User.objects.all()
    sender =request.user.username
    invited_list = invitation.objects.all()
    receiver = User.objects.get(id =id).username
    invite = invitation.objects.create(sender = sender, receiver = receiver)
    invite.invited_by=sender
    invite.save()
    return redirect('home')
@login_required
def Home(request):
    users = User.objects.all()
    abc = invitation.objects.all()
    invited_list=[]
    data = []
    for i in users:
        if i.username != request.user.username :
            data.append(i)
    for i in abc:
        if i.receiver == request.user.username and i.status=='pending':
            invited_list.append(i)

    return render(request,'base.html',{'data':data,'invited_list':invited_list})

@login_required
def view_invitation(request):
    data = User.objects.all()
    invited_list = invitation.objects.all()
    return render(request,'base.html',{'data':data,'invited_list':invited_list})


def Accept_invitation(request,id):
    friend_request = invitation.objects.get(id=id)
    if friend_request.receiver == request.user.username and friend_request.status == 'pending':
        friend_request.status ='Accepted'
        friend_request.save()
        Friendship.objects.create(user1=friend_request.sender, user2=friend_request.receiver)
    return redirect('chat')


def Cancel_invitation(request,id):
    friend_request = invitation.objects.get(id=id)
    if friend_request.receiver == request.user.username and friend_request.status == 'pending':
        friend_request.status ='cancelled'
        friend_request.save()
    return redirect('home')


def ChatRoom(request):
    users = User.objects.all()
    data = []
    for i in users:
        if i.username != request.user.username :
            data.append(i)
    return render(request,'chat.html',{'users':data})

def individuachat(request,name):
    if request.method == 'POST':
        message=request.POST['message']
        chat=Chat.objects.create(
        message = message,
        sender = request.user.username,
        receiver = name,
        date = current_date
        )
        chat.save()
    users = User.objects.all()
    chatdata = Chat.objects.all()
    current= User.objects.get(username=name)
    data = []
    chat=[]
    for i in users:
        if i.username != request.user.username :
            data.append(i)

    for i in chatdata:
        if (i.sender == current.username and i.receiver==request.user.username)  or (i.sender ==request.user.username and i.receiver==current.username):
            # chat.append(i)
            val={}
            val['message']=i.message
            val['name']=i.sender
            val['date']=i.date
            chat.append(val)


    return render(request,'chat.html',{'users':data,'chat':chat,'name':name})

    
def searchUser(request):
    data = User.objects.all()
    print(data)
    return render(request,'base.html',{'data':data})


    