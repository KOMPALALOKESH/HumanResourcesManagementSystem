# Generated by Django 5.1.1 on 2024-09-30 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField()),
                ("status", models.CharField(max_length=10)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee_management.employee",
                    ),
                ),
            ],
        ),
    ]
