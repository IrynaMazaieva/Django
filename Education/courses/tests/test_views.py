import pytest
from model_bakery import baker
from courses import models, views, serializers
from django.contrib.auth.models import User, Group
from django.urls import reverse
from Education import settings
import requests


pytestmark = pytest.mark.django_db

@pytest.fixture
def user_client(api_client):
    user = baker.make(User)
    api_client.force_login(user)
    return api_client

@pytest.fixture
def manager_client(api_client):
    user = baker.make(User)
    group, _ = Group.objects.get_or_create(name=settings.MANAGER_GROUP)
    user.groups.add(group)
    api_client.force_login(user)
    return api_client

@pytest.fixture
def editor_client(api_client):
    user = baker.make(User)
    group, _ = Group.objects.get_or_create(name=settings.EDITOR_GROUP)
    user.groups.add(group)
    api_client.force_login(user)
    return api_client

@pytest.fixture
def student_client(api_client):
    user = baker.make(User)
    group, _ = Group.objects.get_or_create(name=settings.STUDENT_GROUP)
    user.groups.add(group)
    api_client.force_login(user)
    return api_client

@pytest.fixture
def lesson_url():
    return reverse('lesson')

@pytest.fixture
def test_url():
    return reverse('test')

@pytest.fixture
def question_url():
    return reverse('question')

@pytest.fixture
def programm_url():
    return reverse('programm')

@pytest.fixture
def theme_url():
    return reverse('theme')

@pytest.fixture
def student_url():
    return reverse('student')

@pytest.fixture
def user_url():
    return reverse('user')

@pytest.fixture
def lesson_approved_url():
    return reverse('lesson_approved')

@pytest.fixture
def testing_url():
    return reverse('testing')


#  GET

def test_lesson_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, lesson_url):
    assert admin_client.get(lesson_url).status_code == 200
    assert api_client.get(lesson_url).status_code == 200
    assert user_client.get(lesson_url).status_code == 200
    assert manager_client.get(lesson_url).status_code == 200
    assert student_client.get(lesson_url).status_code == 200
    assert editor_client.get(lesson_url).status_code == 200

def test_single_lesson_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, lesson_url):
    lesson = baker.make(models.Lesson)
    assert admin_client.get(lesson_url + str(lesson.id)).status_code == 200
    assert api_client.get(lesson_url + str(lesson.id)).status_code == 200
    assert user_client.get(lesson_url + str(lesson.id)).status_code == 200
    assert manager_client.get(lesson_url + str(lesson.id)).status_code == 200
    assert student_client.get(lesson_url + str(lesson.id)).status_code == 200
    assert editor_client.get(lesson_url + str(lesson.id)).status_code == 200

def test_test_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, test_url):
    assert admin_client.get(test_url).status_code == 200
    assert api_client.get(test_url).status_code == 200
    assert user_client.get(test_url).status_code == 200
    assert manager_client.get(test_url).status_code == 200
    assert student_client.get(test_url).status_code == 200
    assert editor_client.get(test_url).status_code == 200

def test_single_test_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, test_url):
    test = baker.make(models.Test)
    assert admin_client.get(test_url + str(test.id)).status_code == 200
    assert api_client.get(test_url + str(test.id)).status_code == 200
    assert user_client.get(test_url + str(test.id)).status_code == 200
    assert manager_client.get(test_url + str(test.id)).status_code == 200
    assert student_client.get(test_url + str(test.id)).status_code == 200
    assert editor_client.get(test_url + str(test.id)).status_code == 200

def test_question_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, question_url):
    assert admin_client.get(question_url).status_code == 200
    assert api_client.get(question_url).status_code == 200
    assert user_client.get(question_url).status_code == 200
    assert manager_client.get(question_url).status_code == 200
    assert student_client.get(question_url).status_code == 200
    assert editor_client.get(question_url).status_code == 200

def test_single_question_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, question_url):
    question = baker.make(models.Question)
    assert admin_client.get(question_url + str(question.id)).status_code == 200
    assert api_client.get(question_url + str(question.id)).status_code == 200
    assert user_client.get(question_url + str(question.id)).status_code == 200
    assert manager_client.get(question_url + str(question.id)).status_code == 200
    assert student_client.get(question_url + str(question.id)).status_code == 200
    assert editor_client.get(question_url + str(question.id)).status_code == 200

def test_programm_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, programm_url):
    assert admin_client.get(programm_url).status_code == 200
    assert api_client.get(programm_url).status_code == 200
    assert user_client.get(programm_url).status_code == 200
    assert manager_client.get(programm_url).status_code == 200
    assert student_client.get(programm_url).status_code == 200
    assert editor_client.get(programm_url).status_code == 200

def test_single_programm_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, programm_url):
    programm = baker.make(models.Programm)
    assert admin_client.get(programm_url + str(programm.id)).status_code == 200
    assert api_client.get(programm_url + str(programm.id)).status_code == 200
    assert user_client.get(programm_url + str(programm.id)).status_code == 200
    assert manager_client.get(programm_url + str(programm.id)).status_code == 200
    assert student_client.get(programm_url + str(programm.id)).status_code == 200
    assert editor_client.get(programm_url + str(programm.id)).status_code == 200

def test_theme_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, theme_url):
    assert admin_client.get(theme_url).status_code == 200
    assert api_client.get(theme_url).status_code == 200
    assert user_client.get(theme_url).status_code == 200
    assert manager_client.get(theme_url).status_code == 200
    assert student_client.get(theme_url).status_code == 200
    assert editor_client.get(theme_url).status_code == 200

def test_single_theme_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, theme_url):
    theme = baker.make(models.Theme)
    assert admin_client.get(theme_url + str(theme.id)).status_code == 200
    assert api_client.get(theme_url + str(theme.id)).status_code == 200
    assert user_client.get(theme_url + str(theme.id)).status_code == 200
    assert manager_client.get(theme_url + str(theme.id)).status_code == 200
    assert student_client.get(theme_url + str(theme.id)).status_code == 200
    assert editor_client.get(theme_url + str(theme.id)).status_code == 200

def test_student_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, student_url):
    assert admin_client.get(student_url).status_code == 200
    assert api_client.get(student_url).status_code == 200
    assert user_client.get(student_url).status_code == 200
    assert manager_client.get(student_url).status_code == 200
    assert student_client.get(student_url).status_code == 200
    assert editor_client.get(student_url).status_code == 200

def test_single_student_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, student_url):
    student = baker.make(models.Student)
    assert admin_client.get(student_url + str(student.id)).status_code == 200
    assert api_client.get(student_url + str(student.id)).status_code == 200
    assert user_client.get(student_url + str(student.id)).status_code == 200
    assert manager_client.get(student_url + str(student.id)).status_code == 200
    assert student_client.get(student_url + str(student.id)).status_code == 200
    assert editor_client.get(student_url + str(student.id)).status_code == 200

def test_user_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, user_url):
    assert admin_client.get(user_url).status_code == 200
    assert api_client.get(user_url).status_code == 200
    assert user_client.get(user_url).status_code == 200
    assert manager_client.get(user_url).status_code == 200
    assert student_client.get(user_url).status_code == 200
    assert editor_client.get(user_url).status_code == 200

def test_single_user_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, user_url):
    user = baker.make(models.User)
    assert admin_client.get(user_url + str(user.id)).status_code == 200
    assert api_client.get(user_url + str(user.id)).status_code == 200
    assert user_client.get(user_url + str(user.id)).status_code == 200
    assert manager_client.get(user_url + str(user.id)).status_code == 200
    assert student_client.get(user_url + str(user.id)).status_code == 200
    assert editor_client.get(user_url + str(user.id)).status_code == 200

def test_lesson_approved_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, lesson_approved_url):
    assert admin_client.get(lesson_approved_url).status_code == 200
    assert api_client.get(lesson_approved_url).status_code == 200
    assert user_client.get(lesson_approved_url).status_code == 200
    assert manager_client.get(lesson_approved_url).status_code == 200
    assert student_client.get(lesson_approved_url).status_code == 200
    assert editor_client.get(lesson_approved_url).status_code == 200

def test_single_lesson_approved_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, lesson_approved_url):
    lesson_approved = baker.make(models.Lesson)
    assert admin_client.get(lesson_approved_url + str(lesson_approved.id)).status_code == 200
    assert api_client.get(lesson_approved_url + str(lesson_approved.id)).status_code == 200
    assert user_client.get(lesson_approved_url + str(lesson_approved.id)).status_code == 200
    assert manager_client.get(lesson_approved_url + str(lesson_approved.id)).status_code == 200
    assert student_client.get(lesson_approved_url + str(lesson_approved.id)).status_code == 200
    assert editor_client.get(lesson_approved_url + str(lesson_approved.id)).status_code == 200

def test_testing_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, testing_url):
    assert admin_client.get(testing_url).status_code == 200
    assert api_client.get(testing_url).status_code == 200
    assert user_client.get(testing_url).status_code == 200
    assert manager_client.get(testing_url).status_code == 200
    assert student_client.get(testing_url).status_code == 200
    assert editor_client.get(testing_url).status_code == 200

def test_single_testing_view(user_client, manager_client, editor_client, student_client,
                     api_client, admin_client, testing_url):
    test = baker.make(models.Test)
    assert admin_client.get(testing_url + str(test.id)).status_code == 200
    assert api_client.get(testing_url + str(test.id)).status_code == 200
    assert user_client.get(testing_url + str(test.id)).status_code == 200
    assert manager_client.get(testing_url + str(test.id)).status_code == 200
    assert student_client.get(testing_url + str(test.id)).status_code == 200
    assert editor_client.get(testing_url + str(test.id)).status_code == 200
