# Generated by Django 3.2 on 2022-11-05 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
