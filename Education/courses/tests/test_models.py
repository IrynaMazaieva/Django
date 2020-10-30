import pytest
from model_bakery import baker
from courses import models
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db

def test_my_user():
    my_user = baker.make(User)
    assert str(my_user)

def test_theme():
    theme = baker.make(models.Theme)
    assert str(theme)

def test_question():
    question = baker.make(models.Question)
    assert str(question)

def test_programm():
    programm = baker.make(models.Programm)
    assert str(programm)

def test_lesson():
    editor = baker.make(User)
    manager = baker.make(User)
    lesson = baker.make(models.Lesson, editor=editor, manager=manager)
    assert str(lesson)

def test_student():
    student = baker.make(models.Student)
    assert str(student)

def test_test():
    programm = baker.make(models.Programm)
    q1 = baker.make(models.Question, right_var=1, answer=2)
    q2 = baker.make(models.Question, right_var=2)
    test = baker.make(models.Test, programm=programm, questions=[q1, q2], score_to_pass=2)

    assert test.testing
    assert str(test)
