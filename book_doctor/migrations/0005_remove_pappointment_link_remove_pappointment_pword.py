# Generated by Django 4.0 on 2022-01-20 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_doctor', '0004_phydoc_phyapp_pappointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pappointment',
            name='link',
        ),
        migrations.RemoveField(
            model_name='pappointment',
            name='pword',
        ),
    ]
