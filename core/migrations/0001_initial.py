# Generated by Django 4.2.7 on 2024-03-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("cid", models.IntegerField(blank=True, default=0, null=True)),
                ("message", models.TextField(blank=True, max_length=900, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GPSData",
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
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("timestamp", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
