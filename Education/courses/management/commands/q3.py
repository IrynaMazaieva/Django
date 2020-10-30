from django.core.management.base import BaseCommand, CommandError
from courses.models import MyUser, Programm, Lesson


class Command(BaseCommand):
    help = 'List of approved activities for this editor for this programm'

    def add_arguments(self, parser):
        parser.add_argument('editor', type=str)
        parser.add_argument('programm', type=str)

    def handle(self, *args, **options):
        editor = options['editor']
        programm = options['programm']

        try:
            MyUser.objects.filter(username=editor).get()
        except MyUser.DoesNotExist:
            raise CommandError("No such editor!!!")

        try:
            Programm.objects.filter(programm_name=programm).get()
        except Programm.DoesNotExist:
            raise CommandError("No such programm!!!")

        lessons = Lesson.objects.filter(editor__username=editor).filter(
            programm__programm_name=programm).filter(is_approved=True)

        self.stdout.write(str(lessons))
