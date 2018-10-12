from django.contrib import admin
from .models import Subject, Grade, Teacher, Lesson, MainModel, Pupil, Room, Schedule

# Register your models here.

admin.site.register(Pupil)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Room)
admin.site.register(Lesson)
admin.site.register(Schedule)
