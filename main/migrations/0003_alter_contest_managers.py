# Generated by Django 4.1.7 on 2023-10-30 16:52

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_user_options_alter_checker_table_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="contest",
            managers=[
                ("Contest", django.db.models.manager.Manager()),
            ],
        ),
    ]
