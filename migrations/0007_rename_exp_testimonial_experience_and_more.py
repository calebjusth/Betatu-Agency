# Generated by Django 4.1.1 on 2022-11-26 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitatu', '0006_rename_testimonials_testimonial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='exp',
            new_name='experience',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='name_of_test',
            new_name='name_of_testifier',
        ),
    ]
