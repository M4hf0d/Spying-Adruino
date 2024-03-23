# Generated by Django 4.2.7 on 2024-03-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_gpsdata_timestamp"),
    ]

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
    ]
