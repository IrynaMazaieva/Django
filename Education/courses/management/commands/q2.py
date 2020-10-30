from django.core.management.base import BaseCommand, CommandError
from courses.models import Programm, Student


class Command(BaseCommand):
    help = 'Select a list of students who are subscribed to a given program'

    def add_arguments(self, parser):
        parser.add_argument('programm', type=str)

    def handle(self, *args, **options):
        programm = options['programm']

        try:
            programm_obj = Programm.objects.filter(programm_name=programm)
            programm_obj.get()
        except Programm.DoesNotExist:
            raise CommandError("No such students programm!!!")

        programm_obj = Student.objects.filter(programm__programm_name=programm)
        ans = ''
        for i in programm_obj:
            ans += '\n' + str(i.user)
        self.stdout.write(ans)
