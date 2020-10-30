from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    theme_name = models.CharField(max_length=60)

    def __str__(self):
        return self.theme_name


class Question(models.Model):
    question = models.TextField(verbose_name='The question is: ')
    var_1 = models.TextField(verbose_name='First variant: ')
    var_2 = models.TextField(verbose_name='Second variant: ')
    var_3 = models.TextField(verbose_name='Third variant: ')
    right_var = models.IntegerField(verbose_name='Number of right variant: ')
    CHOICES = [(1, str(var_1)), (2, str(var_2)), (3, str(var_3))]
    answer = models.IntegerField(choices=CHOICES, null=True)

    def testing_q(self, answer, right_var):
        if answer == right_var:
            return True
        return False

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Question for testing students'


class Programm(models.Model):
    programm_name = models.CharField(max_length=60)

    def __str__(self):
        return self.programm_name


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=60)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, blank=True, null=True)
    programm = models.ForeignKey(Programm, on_delete=models.SET_NULL, null=True)
    previous_lesson = models.ForeignKey('self', related_name='my_lessons_previous_lesson_set',
                                        on_delete=models.CASCADE, blank=True, null=True)
    previous_version = models.ForeignKey('self', related_name='my_lessons_previous_version_set',
                                         on_delete=models.CASCADE, blank=True, null=True)
    next_version = models.ForeignKey('self', related_name='my_lessons_next_version_set',
                                     on_delete=models.CASCADE, blank=True, null=True)

    theory = models.TextField()
    practice = models.TextField()

    is_approved = models.BooleanField(default=False)

    editor = models.ForeignKey(User, related_name='my_lessons_editor_set', on_delete=models.CASCADE)
    manager = models.ForeignKey(User, related_name='my_lessons_manager_set', on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_name


class Student(models.Model):
    programm = models.ManyToManyField(Programm)
    user = models.ForeignKey(User, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Test(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tests')
    programm = models.ForeignKey(Programm, on_delete=models.CASCADE, related_name='tests')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tests')
    questions = models.ManyToManyField(Question, related_name='tests')
    score_to_pass = models.IntegerField(verbose_name='Score to pass test')


    @property
    def testing(self):
        score = 0
        is_passed = False
        for q in self.questions.all():
            if q.testing_q:
                score += 1
        if score >= self.score_to_pass:
            is_passed = True
        return is_passed

    is_passed = testing

    def __str__(self):
        return '{}, {}'.format(self.student, self.lesson)
