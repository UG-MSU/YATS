# Generated by Django 4.2.6 on 2023-10-30 12:45

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import main.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="user",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("patronymic", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("school", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                (
                    "role",
                    models.IntegerField(
                        choices=[
                            (1, "Admin"),
                            (2, "Teacher"),
                            (3, "Student"),
                            (4, "Parent"),
                        ],
                        default=3,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="contest",
            fields=[
                ("id_contest", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255)),
                ("description", models.CharField(blank=True, max_length=1000)),
                ("password", models.CharField(blank=True, max_length=25)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MyModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("upload", models.FileField(upload_to=main.models.user_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name="report_sub",
            fields=[
                (
                    "id_report_sub",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("type", models.IntegerField(blank=True)),
                ("text_sub", models.CharField(blank=True, max_length=255)),
                ("pend_rew", models.CharField(blank=True, max_length=255)),
            ],
            managers=[
                ("Report_sub", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="task",
            fields=[
                ("id_task", models.BigAutoField(primary_key=True, serialize=False)),
                ("task_name", models.CharField(blank=True, max_length=255)),
                ("statement", models.CharField(blank=True, max_length=300)),
            ],
            managers=[
                ("Task", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="test",
            fields=[
                ("id_test", models.BigAutoField(primary_key=True, serialize=False)),
                ("pathToFileWithTests", models.CharField(blank=True, max_length=255)),
                (
                    "id_task",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.task",
                    ),
                ),
            ],
            managers=[
                ("Test", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="submission",
            fields=[
                ("id_sub", models.BigAutoField(primary_key=True, serialize=False)),
                ("timestamp", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("WRONG ANSWER", "Wa"),
                            ("COMPILATION ERROR", "Ce"),
                            ("TIME LIMIT", "Tl"),
                            ("MEMORY LIMIT", "Ml"),
                            ("OK", "Ok"),
                            ("NOT CHECKED", "Nc"),
                        ],
                        default="NOT CHECKED",
                        max_length=17,
                    ),
                ),
                ("executable_path", models.CharField(blank=True, max_length=255)),
                ("lang", models.CharField(blank=True, max_length=255)),
                (
                    "id_contest",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.contest",
                    ),
                ),
                (
                    "id_task",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.task",
                    ),
                ),
                (
                    "id_user",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            managers=[
                ("Submission", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="review_message",
            fields=[
                (
                    "id_review_message",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("rew", models.CharField(blank=True, max_length=255)),
                (
                    "id_report_sub",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.report_sub",
                    ),
                ),
            ],
            managers=[
                ("Review_message", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name="report_sub",
            name="id_sub",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.submission",
            ),
        ),
        migrations.CreateModel(
            name="legend",
            fields=[
                ("id_legend", models.BigAutoField(primary_key=True, serialize=False)),
                ("text", models.CharField(blank=True, max_length=255)),
                (
                    "id_contest",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.contest",
                    ),
                ),
                (
                    "id_task",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.task",
                    ),
                ),
            ],
            managers=[
                ("Legend", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="contest_user",
            fields=[
                (
                    "id_contest_user",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "id_contest",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.contest",
                    ),
                ),
                (
                    "id_user",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            managers=[
                ("Contest_user", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="contest_task",
            fields=[
                (
                    "id_contest_task",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "id_contest",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.contest",
                    ),
                ),
                (
                    "id_task",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.task",
                    ),
                ),
            ],
            managers=[
                ("Contest_task", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="checker",
            fields=[
                ("id_checker", models.BigAutoField(primary_key=True, serialize=False)),
                ("prog_path", models.CharField(blank=True, max_length=255)),
                (
                    "id_task",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.task",
                    ),
                ),
            ],
            managers=[
                ("Checker", django.db.models.manager.Manager()),
            ],
        ),
    ]
