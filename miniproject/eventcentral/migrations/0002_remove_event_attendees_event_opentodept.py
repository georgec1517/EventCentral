# Generated by Django 4.2.1 on 2023-05-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventcentral', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendees',
        ),
        migrations.AddField(
            model_name='event',
            name='opentodept',
            field=models.CharField(choices=[('cse', 'CSE'), ('me', 'ME'), ('ce', 'CE'), ('eee', 'EEE'), ('ece', 'ECE'), ('cidrie', 'CIDRIE'), ('open', 'OPEN')], default='open', max_length=6),
        ),
    ]
