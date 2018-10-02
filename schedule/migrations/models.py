from django.db import models


class Pupil(models.Model):
    lastname = models.CharField(max_lenght=32)
    firstname = models.CharField(max_lenght=32)
    surname = models.CharField(max_lenght=32)
    grade = models.CharField(max_lenght=4)


class Teacher(models.Model):
    lastname = models.CharField(max_lenght=32)
    firstname = models.CharField(max_lenght=32)
    surname = models.CharField(max_lenght=32)


class Grade(models.Model):
    name = models.CharField(max_lenght=4)
    lead = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)


class Room(models.Model):
    number = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)


class Subject(models.Model):
    name = models.CharField(max_lenght=32)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)


class Lesson(models.Model):
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)


class Schedule(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField()
