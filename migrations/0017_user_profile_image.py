# Generated by Django 4.1.1 on 2022-12-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitatu', '0016_user_profile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(default=False, upload_to='profiles/'),
        ),
    ]
