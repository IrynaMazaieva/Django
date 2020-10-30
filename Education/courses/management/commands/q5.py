from django.core.management.base import BaseCommand, CommandError
from courses.models import Student, Lesson, Test
from django.db.models import Prefetch


class Command(BaseCommand):
    help = 'List of current classes (which need to be taken at the moment) for all programs for this student'

    def add_arguments(self, parser):
        parser.add_argument('student', type=str)

    def handle(self, *args, **options):
        student = options['student']

        try:
            Student.objects.get(user__username=student)
        except Student.DoesNotExist:
            raise CommandError("No such student!!!")

        programms = Student.objects.filter(user__username=student).first().programm.all()

        lessons = Lesson.objects.prefetch_related(Prefetch('programm', queryset=programms))
        tests = Test.objects.filter(student__user__username=student).prefetch_related(
            Prefetch('lesson', queryset=lessons))
        for test in tests:
            lessons = lessons.exclude(lesson_name=test.lesson)

        result = Lesson.objects.none()
        for programm in programms:
            query = lessons.filter(lesson_name=lessons.filter(programm=programm).first())
            if query:
                result = result.union(query)

        print(result)
