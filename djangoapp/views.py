from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail,EmailMessage
from django.core.mail import settings

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






def send_invitation(request):
    return render(request,'invitation.html')