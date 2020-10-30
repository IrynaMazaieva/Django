from rest_framework import serializers
from .models import (
    Lesson,
    Question,
    Test,
    Student,
    Programm,
    Theme,
)
from django.contrib.auth.models import User

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = [
            'id', 'lesson_name', 'theme', 'programm',
            'previous_lesson',
            'previous_version', 'next_version',
            'theory', 'practice',
            'editor', 'manager', 'is_approved'
        ]
        read_only_fields = ['is_approved']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'student', 'programm', 'lesson', 'score_to_pass', 'questions']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class QuestionForTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'question', 'var_1', 'var_2', 'var_3', 'answer']
        read_only_fields = ['id', 'question', 'var_1', 'var_2', 'var_3']


class TestingStudentSerializer(serializers.ModelSerializer):
    questions = QuestionForTestSerializer(many=True)

    class Meta:
        model = Test
        fields = ['programm', 'lesson', 'score_to_pass', 'questions']
        read_only_fields = ['programm', 'lesson', 'score_to_pass']


class ProgrammSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programm
        fields = ['id', 'programm_name']


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'


class LessonApprovedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = [
            'id', 'lesson_name', 'theme', 'programm',
            'previous_lesson',
            'previous_version', 'next_version',
            'theory', 'practice',
            'editor', 'manager', 'is_approved'
        ]
        read_only_fields = [
            'id', 'lesson_name', 'theme', 'programm',
            'previous_lesson',
            'previous_version', 'next_version',
            'theory', 'practice',
            'editor', 'manager', 'is_approved'
        ]


class Q6Serializer(serializers.Serializer):
    child = StudentSerializer
    student_dict = serializers.DictField()
