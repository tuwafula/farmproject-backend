# Generated by Django 4.1.2 on 2022-10-27 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_farmerprofile_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenderprofile',
            name='phone_number',
        ),
    ]
