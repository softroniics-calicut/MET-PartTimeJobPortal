# Generated by Django 3.2.23 on 2024-01-04 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0005_auto_20240103_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='password',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='username',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
    ]
