# Generated by Django 4.2.7 on 2024-06-11 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("u_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("u_fullname", models.CharField(max_length=200, null=True)),
                ("u_nickname", models.CharField(max_length=200, null=True)),
                ("u_email", models.CharField(max_length=200, null=True, unique=True)),
                ("u_password", models.CharField(max_length=200)),
                ("u_whatsapp_number", models.CharField(max_length=200, null=True)),
                (
                    "u_created_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024, 6, 11, 11, 27, 58, 92333, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "u_updated_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024, 6, 11, 11, 27, 58, 92638, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "u_deleted_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024, 6, 11, 11, 27, 58, 92651, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                ("u_created_by", models.CharField(max_length=200, null=True)),
                ("u_updated_by", models.CharField(max_length=200, null=True)),
                ("u_deleted_by", models.CharField(max_length=200, null=True)),
            ],
            options={
                "db_table": "users",
            },
        ),
    ]