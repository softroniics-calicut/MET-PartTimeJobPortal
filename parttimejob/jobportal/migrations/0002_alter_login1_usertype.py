# Generated by Django 3.2.23 on 2024-01-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login1',
            name='usertype',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
