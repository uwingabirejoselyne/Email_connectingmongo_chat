from django.contrib import admin
from .models import *

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ('id','studentId','first_name','last_name','email')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','courseId','coursename',)


class ChaptersAdmin(admin.ModelAdmin):
    list_display = ('id','chapterId','courseId','chaptertitle','Description')


class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','sender','receiver')


class InvitationAdmin(admin.ModelAdmin):
    list_display = ('id','sender','receiver','status')

admin.site.register(Students)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapters, ChaptersAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(invitation, InvitationAdmin)


