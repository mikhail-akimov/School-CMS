from django.contrib import admin
from .models import Subject, Grade, Teacher, Lesson, MainModel, Pupil, Room, Schedule


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'surname', 'pup_grade')
    list_filter = ('lastname', 'firstname', 'surname', 'pup_grade')
    fields = [('lastname', 'firstname', 'surname'), 'pup_grade']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'surname')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_subject_teacher')
    list_filter = ('name',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('display_lesson', 'weekday', 'starttime')
    list_filter = ('weekday', 'starttime')


# Register the admin class with the associated model


# admin.site.register(Pupil, PupilAdmin)
# admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(Grade, GradeAdmin)


# Register your models here.

# admin.site.register(Pupil)
# admin.site.register(Teacher)
# admin.site.register(Grade)
# admin.site.register(Subject)
# admin.site.register(Room)
# admin.site.register(Lesson)
# admin.site.register(Schedule)
