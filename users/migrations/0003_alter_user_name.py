# Generated by Django 4.1.1 on 2022-09-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_is_host_user_name_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(default="", max_length=150),
        ),
    ]