from django.contrib import admin
from .models import (
    Lesson,
    Question,
    Test,
    Student,
    Programm,
    Theme,
)


class LessonAdmin(admin.ModelAdmin):
    list_display = ['lesson_name', 'programm', 'previous_lesson', 'theme', 'editor', 'manager', 'is_approved']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class ProgrammAdmin(admin.ModelAdmin):
    list_display = ['programm_name']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', ]


class TestAdmin(admin.ModelAdmin):
    list_display = ['student', 'programm', 'lesson', 'is_passed']


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Theme)
admin.site.register(Programm, ProgrammAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Test, TestAdmin)
