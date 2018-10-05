from django.db import models


class MainModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(auto_now=True)


class Pupil(MainModel):
    lastname = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    pup_grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)


class Teacher(MainModel):
    lastname = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)


class Grade(MainModel):
    name = models.CharField(max_length=4)
    lead = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)


class Room(MainModel):
    number = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)


class Subject(MainModel):
    name = models.CharField(max_length=32)
    subj_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)


class Lesson(MainModel):
    les_grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)
    les_subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    les_room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)


class Schedule(MainModel):
    plan_lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField()
