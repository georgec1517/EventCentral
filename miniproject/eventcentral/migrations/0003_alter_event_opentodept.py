# Generated by Django 4.2.1 on 2023-05-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventcentral', '0002_remove_event_attendees_event_opentodept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='opentodept',
            field=models.CharField(choices=[('Computer Science and Engineering', 'CSE'), ('Mechanical Engineering', 'ME'), ('Civil Engineering', 'CE'), ('Electrical Engineering', 'EEE'), ('Electronics and Communication', 'ECE'), ('CIDRIE', 'CIDRIE'), ('All Departments', 'OPEN')], max_length=50),
        ),
    ]
