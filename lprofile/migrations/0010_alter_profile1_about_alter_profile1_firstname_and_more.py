# Generated by Django 4.1.6 on 2023-05-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lprofile', '0009_profile1_profowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile1',
            name='about',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile1',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile1',
            name='lastname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
