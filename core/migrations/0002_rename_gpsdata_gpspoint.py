# Generated by Django 4.2.7 on 2024-05-09 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="GPSData",
            new_name="GpsPoint",
        ),
    ]
