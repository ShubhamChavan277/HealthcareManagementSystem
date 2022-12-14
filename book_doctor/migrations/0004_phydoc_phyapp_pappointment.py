# Generated by Django 4.0 on 2022-01-20 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_log_id_alter_logd_id'),
        ('book_doctor', '0003_alter_vappointment_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhyDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='PhyApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(choices=[(0, '09:00 - 09:30'), (1, '10:00 - 10:30'), (2, '11:00 - 11:30'), (3, '12:00 - 12:30'), (4, '13:00 - 13:30'), (5, '14:00 - 14:30'), (6, '15:00 - 15:30'), (7, '16:00 - 16:30'), (8, '17:00 - 17:30')])),
                ('phydoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_doctor.phydoc')),
            ],
        ),
        migrations.CreateModel(
            name='PAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tslot', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('link', models.URLField()),
                ('pword', models.CharField(max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_doctor.doctor')),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.log')),
            ],
        ),
    ]
