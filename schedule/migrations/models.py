class Pupil():
    lastname = models.CharField(max_lenght=32)
    firstname = models.CharField(max_lenght=32)
    surname = models.CharField(max_lenght=32)
    grade = models.CharField(max_lenght=4)


class Teacher():
    lastname = models.CharField(max_lenght=32)
    firstname = models.CharField(max_lenght=32)
    surname = models.CharField(max_lenght=32)


class Grade():
    name = models.CharField(max_lenght=4)
    lead = models.SmallIntegerFiled() # Teacher.id


class Room():
    number = models.SmallIntegerFiled(max_lenght=3)


class Subject():
    name = models.CharField(max_lenght=32)
    teacher = models.SmallIntegerFiled()  # Teacher.id


class Lesson():
    grade = models.SmallIntegerFiled() # Grade.id
    subject = models.SmallIntegerFiled() # Subject.id
    room = models.SmallIntegerFiled() # Room.id


class Schedule():
    lesson = models.SmallIntegerFiled() # Lesson.id
    datetime = models.DateTimeField()