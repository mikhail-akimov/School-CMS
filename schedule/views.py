from django.shortcuts import render, render_to_response
from .models import Pupil, Teacher, Grade, Lesson, Room, Schedule, DAY_OW_THE_WEEK, LESSON_START_TIME
# Create your views here.



def main_view(request):
    name = 'Mikhail'
    schedule = Schedule.objects.all()
    weekday = DAY_OW_THE_WEEK
    starttime = LESSON_START_TIME
    grade = Grade.objects.all()
    return render_to_response('index.html', {'schedule': schedule, 'name': name, 'weekday': weekday, 'starttime': starttime, 'grade': grade})
