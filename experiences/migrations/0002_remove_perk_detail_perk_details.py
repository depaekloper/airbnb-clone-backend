# Generated by Django 4.1.1 on 2022-09-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="perk",
            name="detail",
        ),
        migrations.AddField(
            model_name="perk",
            name="details",
            field=models.CharField(blank=True, default="", max_length=250),
        ),
    ]