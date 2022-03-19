# Generated by Django 3.2.9 on 2022-03-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_userprofile_user'),
        ('events', '0006_alter_event_participantes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participantes',
        ),
        migrations.AddField(
            model_name='event',
            name='entry',
            field=models.ManyToManyField(blank=True, to='user.UserProfile'),
        ),
    ]
