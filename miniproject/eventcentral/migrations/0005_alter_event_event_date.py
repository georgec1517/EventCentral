# Generated by Django 4.2.1 on 2023-05-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventcentral', '0004_event_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(verbose_name='Event Date'),
        ),
    ]
