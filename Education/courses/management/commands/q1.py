from django.core.management.base import BaseCommand, CommandError
from courses.models import Student, Test


class Command(BaseCommand):
    help = 'Select a list of available assignments for this student and this program'

    def add_arguments(self, parser):
        parser.add_argument('student', type=str)
        parser.add_argument('programm', type=int)

    def handle(self, *args, **options):
        name = options['student']
        programm = options['programm']

        try:
            Student.objects.get(user__username=name)
        except Student.DoesNotExist:
            raise CommandError("No such student!!!")

        try:
            Student.objects.filter(user__username=name).get(programm__id=programm)
        except Student.DoesNotExist:
            raise CommandError("No such students programm!!!")

        tests = Test.objects.filter(student__user__username=name).filter(
            lesson__is_approved=True).filter(programm__id=programm).all()

        print(tests)
