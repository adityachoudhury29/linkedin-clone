# Generated by Django 4.1.6 on 2023-05-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lprofile', '0023_posts_postimg_profile1_profimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='postimg',
            field=models.ImageField(blank=True, null=True, upload_to='media/postimages'),
        ),
        migrations.AlterField(
            model_name='profile1',
            name='profimg',
            field=models.ImageField(blank=True, null=True, upload_to='media/profimages'),
        ),
    ]
