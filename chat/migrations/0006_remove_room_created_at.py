# Generated by Django 4.2.2 on 2023-06-30 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_room_messages_roomname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='created_at',
        ),
    ]