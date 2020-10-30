from django.core.management.base import BaseCommand
from courses.models import Programm, Student


class Command(BaseCommand):
    help = 'List of programs with the number of students who are subscribed to them'

    def handle(self, *args, **options):
        programms = Programm.objects.all()
        programm_dict = {}
        for programm in programms:
            programm_dict[programm.programm_name] = Student.objects.filter(programm=programm).count()
        print(programm_dict)
