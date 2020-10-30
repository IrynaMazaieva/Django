from django.core.management.base import BaseCommand
from courses.models import Student, Test


class Command(BaseCommand):
    help = 'List of students with the number of classes they have taken'

    def handle(self, *args, **options):
        students = Student.objects.select_related('user')
        tests = Test.objects.select_related('student')
        student_dict = {}

        for student in students:
            student_dict[student.user.username] = 0
            for student in tests:
                if student.testing:
                    if student.student.user.username in student_dict.keys():
                        student_dict[student.student.user.username] += 1

        print(student_dict)
