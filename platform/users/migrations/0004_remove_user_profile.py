# Generated by Django 3.0.7 on 2020-11-23 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
    ]