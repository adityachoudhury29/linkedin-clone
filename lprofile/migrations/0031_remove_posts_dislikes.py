# Generated by Django 4.2.2 on 2023-07-11 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lprofile', '0030_profile1_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='dislikes',
        ),
    ]
