# Generated by Django 4.1.6 on 2023-06-17 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lprofile', '0028_alter_profile1_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='replies',
        ),
        migrations.AddField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
