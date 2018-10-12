from django.db import models

DAY_OW_THE_WEEK = [
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday')
]

LESSON_START_TIME = [
    ('1', '8:00'),
    ('2', '9:00'),
    ('3', '10:00'),
    ('4', '11:00'),
    ('5', '12:00'),
    ('6', '13:00')
]


class MainModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(auto_now=True)


class Pupil(MainModel):
    lastname = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    pup_grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        self.fi = ('{} {}.'.format(self.lastname, str(self.firstname)[0]))
        return self.fi


class Teacher(MainModel):
    lastname = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self):
        self.fio = ('{} {} {}'.format(self.lastname, self.firstname, self.surname))
        return self.fio


class Grade(MainModel):
    name = models.CharField(max_length=4)
    lead = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Room(MainModel):
    number = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.number)


class Subject(MainModel):
    name = models.CharField(max_length=32)
    subj_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Lesson(MainModel):
    les_grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)
    les_subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    les_room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        self.les_name = ('{} to {}'.format(self.les_subject, self.les_grade))
        return str(self.les_name)


class Schedule(MainModel):
    plan_lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True)
    weekday = models.CharField(max_length=2, choices=DAY_OW_THE_WEEK, null=False, default='1')
    starttime = models.CharField(max_length=2, choices=LESSON_START_TIME, null=False, default='1')

    def __str__(self):
        return str(self.plan_lesson)