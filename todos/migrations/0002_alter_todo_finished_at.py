# Generated by Django 4.1.1 on 2022-10-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="finished_at",
            field=models.DateField(),
        ),
    ]
