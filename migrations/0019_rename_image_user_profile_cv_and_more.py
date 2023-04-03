# Generated by Django 4.1.1 on 2022-12-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitatu', '0018_delete_userregistration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='image',
            new_name='CV',
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='address',
            new_name='experience',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='profile_pic',
            field=models.ImageField(default=False, upload_to='profiles/'),
        ),
    ]
