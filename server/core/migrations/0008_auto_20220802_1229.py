# Generated by Django 3.2.1 on 2022-08-02 06:59

from django.db import migrations
from core.mock_data.user_mock_data import users
from django.contrib.auth.models import User


def create_user(apps, schema_editor):
    for user in users:
        user_to_create = User(
            email=user["email"],
            username=user["user_name"],
            password=user["password"],
        )
        user_to_create.save()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_auto_20220801_1906"),
    ]

    operations = [
        migrations.RunPython(
            create_user,
            lambda _, x: None,
        ),
    ]
