# Generated by Django 3.0.2 on 2020-02-02 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_course_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='location',
            new_name='course_info',
        ),
    ]
