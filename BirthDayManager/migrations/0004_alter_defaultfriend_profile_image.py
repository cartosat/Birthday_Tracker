# Generated by Django 3.2.10 on 2022-11-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BirthDayManager', '0003_defaultfriend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultfriend',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/default-images/user-default.png', null=True, upload_to='profiles/default-images/'),
        ),
    ]
