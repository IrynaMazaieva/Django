from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User

from .models import (
    Lesson,
    Question,
    Test,
    Student,
    Programm,
    Theme,
)
from .serializers import (
    LessonSerializer,
    LessonApprovedSerializer,
    QuestionSerializer,
    TestSerializer,
    TestingStudentSerializer,
    UserSerializer,
    StudentSerializer,
    ProgrammSerializer,
    ThemeSerializer,
)
from .permissions import (
    IsAdmin,
    IsEditor,
    IsManager,
    IsStudent,
    ReadOnly
)


class LessonView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsEditor | ReadOnly]


class SingleLessonView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsEditor | ReadOnly]


class TestView(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdmin | IsEditor | IsManager | ReadOnly]


class SingleTestView(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdmin | IsEditor | IsManager | ReadOnly]


class QuestionView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdmin | IsEditor | IsManager | ReadOnly]


class SingleQuestionView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdmin | IsEditor | IsManager | ReadOnly]


class ProgrammView(ListCreateAPIView):
    queryset = Programm.objects.all()
    serializer_class = ProgrammSerializer
    permission_classes = [IsAdmin | IsEditor | IsManager | ReadOnly]


class SingleProgrammView(RetrieveUpdateDestroyAPIView):
    queryset = Programm.objects.all()
    serializer_class = ProgrammSerializer
    permission_classes = [IsAdmin | IsEditor | IsManager | ReadOnly]


class ThemeView(ListCreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [IsAdmin | IsEditor | IsManager | ReadOnly]


class SingleThemeView(RetrieveUpdateDestroyAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [IsAdmin | IsEditor | IsManager | ReadOnly]


class StudentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsManager | IsEditor | IsAdmin | ReadOnly]


class SingleStudentView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsManager | IsEditor | IsAdmin | ReadOnly]


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin | ReadOnly]


class SingleUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin | ReadOnly]


class LessonApprovedView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonApprovedSerializer
    permission_classes = [IsManager | IsAdmin | ReadOnly]


class SingleLessonApprovedView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonApprovedSerializer
    permission_classes = [IsManager | IsAdmin | ReadOnly]


class TestingStudentView(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestingStudentSerializer
    permission_classes = [IsStudent | ReadOnly]


class SingleTestingStudentView(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestingStudentSerializer
    permission_classes = [IsStudent | ReadOnly]


class Q1(ListAPIView):
    """
        example: http://127.0.0.1:8000/api/q1/?student=student&programm=1
    """

    permission_classes = [IsAdmin | ReadOnly]
    serializer_class = TestSerializer

    def get_queryset(self):
        programm = self.request.query_params.get('programm', None)
        user = self.request.query_params.get('student', None)
        tests = Test.objects.filter(student__user__username=user).filter(
            lesson__is_approved=True).filter(lesson__programm=programm).all()
        return tests


class Q2(ListAPIView):
    """
        example: http://127.0.0.1:8000/api/q2/?programm=1
    """

    serializer_class = StudentSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_queryset(self):
        programm = self.request.query_params.get('programm', None)
        programm_obj = Student.objects.filter(programm__id=programm)
        return programm_obj


class Q3(ListAPIView):
    """
        example: http://127.0.0.1:8000/api/q3/?editor=editor&programm=programm_name0
    """

    serializer_class = LessonSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_queryset(self):
        editor = self.request.query_params.get('editor', None)
        programm = self.request.query_params.get('programm', None)
        lessons = Lesson.objects.filter(editor__username=editor).filter(
            programm__programm_name=programm).filter(is_approved=True)
        return lessons


class Q4(ListAPIView):
    """
        example: http://127.0.0.1:8000/api/q4/
    """

    serializer_class = LessonSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_queryset(self):
        return Lesson.objects.filter(is_approved=False)


class Q5(ListAPIView):
    """
        example: http://127.0.0.1:8000/api/q5/?student=miss
    """

    serializer_class = LessonSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_queryset(self):
        student = self.request.query_params.get('student', None)
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
        return result


class Q6(viewsets.ViewSet):
    """
        example: http://127.0.0.1:8000/api/q6/
    """

    http_method_names = ('get',)
    permission_classes = [IsAdmin | ReadOnly]

    def list(self, request):
        students = Student.objects.select_related('user')
        tests = Test.objects.select_related('student')
        student_dict = {}

        for student in students:
            student_dict[student.user.username] = 0
            for student in tests:
                if student.testing:
                    if student.student.user.username in student_dict.keys():
                        student_dict[student.student.user.username] += 1

        return Response(student_dict)

class Q7(viewsets.ViewSet):
    """
        example: http://127.0.0.1:8000/api/q7/
    """

    http_method_names = ('get',)
    permission_classes = [IsAdmin | ReadOnly]

    def list(self, request):
        programms = Programm.objects.all()
        programm_dict = {}
        for programm in programms:
            programm_dict[programm.programm_name] = Student.objects.filter(programm=programm).count()
        return Response(programm_dict)
