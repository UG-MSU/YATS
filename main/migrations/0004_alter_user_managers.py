# Generated by Django 4.1.7 on 2023-10-30 17:10

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_contest_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("User", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
