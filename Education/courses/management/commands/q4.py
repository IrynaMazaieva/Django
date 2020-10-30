from django.core.management.base import BaseCommand, CommandError
from courses.models import MyUser, Lesson


class Command(BaseCommand):
    help = 'List of new (unapproved) activities for manager review'

    def add_arguments(self, parser):
        parser.add_argument('manager', type=str)

    def handle(self, *args, **options):
        name = options['manager']

        try:
            manager_obj = MyUser.objects.filter(username=name).get()
        except MyUser.DoesNotExist:
            raise CommandError("No such manager!!!")

        lessons = Lesson.objects.filter(is_approved=False).filter(manager=manager_obj)
        ans = ''
        for i in lessons:
            ans += '\n' + i.lesson_name
        self.stdout.write(ans)
