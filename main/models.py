from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager



def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class task(models.Model):
    id_task = models.BigAutoField(primary_key=True)
    task_name = models.CharField(blank=True, max_length=255)
    statement = models.CharField(blank=True, max_length=300)
    Task = models.Manager()

    class Meta:
        db_table = "task"


class user(AbstractUser):
    class ROLES(models.IntegerChoices):
        admin = 1
        teacher = 2
        student = 3
        parent = 4

    patronymic = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    role = models.IntegerField(choices=ROLES.choices, default=ROLES.student)
    User = UserManager()

    class Meta:
        db_table = "user"


class contest(models.Model):
    id_contest = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=255)
    description = models.CharField(max_length=1000, blank=True)
    password = models.CharField(max_length=25, blank=True)
    creator = models.ForeignKey(
        "user", on_delete=models.CASCADE, blank=True, default=""
    )
    Contest = models.Manager()

    class Meta:
        db_table = "contest"

    def __str__(self):
        return self.name


class test(models.Model):
    id_test = models.BigAutoField(primary_key=True)
    id_task = models.ForeignKey("task", on_delete=models.CASCADE, blank=True)
    pathToFileWithTests = models.CharField(blank=True, max_length=255)
    Test = models.Manager()

    class Meta:
        db_table = "test"


class submission(models.Model):
    class STATUS(models.TextChoices):
        wa = "WRONG ANSWER"
        ce = "COMPILATION ERROR"
        tl = "TIME LIMIT"
        ml = "MEMORY LIMIT"
        ok = "OK"
        nc = "NOT CHECKED"

    id_sub = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey("user", on_delete=models.CASCADE, blank=True)
    id_task = models.ForeignKey("task", on_delete=models.CASCADE, blank=True)
    id_contest = models.ForeignKey("contest", on_delete=models.CASCADE, blank=True)
    timestamp = models.DateTimeField()
    status = models.CharField(
        choices=STATUS.choices, blank=True, max_length=17, default=STATUS.nc
    )
    executable_path = models.CharField(blank=True, max_length=255)
    lang = models.CharField(blank=True, max_length=255)
    Submission = models.Manager()

    class Meta:
        db_table = "submission"


class report_sub(models.Model):
    id_report_sub = models.BigAutoField(primary_key=True)
    id_sub = models.ForeignKey("submission", on_delete=models.CASCADE, blank=True)
    type = models.IntegerField(blank=True)
    text_sub = models.CharField(blank=True, max_length=255)
    pend_rew = models.CharField(blank=True, max_length=255)
    Report_sub = models.Manager()

    class Meta:
        db_table = "report_sub"


class review_message(models.Model):
    id_review_message = models.BigAutoField(primary_key=True)
    id_report_sub = models.ForeignKey(
        "report_sub", on_delete=models.CASCADE, blank=True
    )
    rew = models.CharField(blank=True, max_length=255)
    Review_message = models.Manager()

    class Meta:
        db_table = "review_message"


class legend(models.Model):
    id_legend = models.BigAutoField(primary_key=True)
    id_task = models.ForeignKey("task", on_delete=models.CASCADE, blank=True)
    id_contest = models.ForeignKey("contest", on_delete=models.CASCADE, blank=True)
    text = models.CharField(blank=True, max_length=255)
    Legend = models.Manager()

    class Meta:
        db_table = "legend"


class contest_user(models.Model):
    id_contest_user = models.BigAutoField(primary_key=True)
    id_contest = models.ForeignKey("contest", on_delete=models.CASCADE, blank=True)
    id_user = models.ForeignKey("user", on_delete=models.CASCADE, blank=True)
    Contest_user = models.Manager()

    class Meta:
        db_table = "contest_user"


class contest_task(models.Model):
    id_contest_task = models.BigAutoField(primary_key=True)
    id_task = models.ForeignKey("task", on_delete=models.CASCADE, blank=True)
    id_contest = models.ForeignKey("contest", on_delete=models.CASCADE, blank=True)
    Contest_task = models.Manager()

    class Meta:
        db_table = "contest_task"


class checker(models.Model):
    id_checker = models.BigAutoField(primary_key=True)
    prog_path = models.CharField(blank=True, max_length=255)
    id_task = models.ForeignKey("task", on_delete=models.CASCADE, blank=True)
    Checker = models.Manager()

    class Meta:
        db_table = "checker"


class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
