# Generated by Django 4.1.1 on 2022-11-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitatu', '0004_remove_blog_breakdown_remove_blog_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.TextField()),
                ('name_of_test', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='password1',
            field=models.CharField(max_length=20),
        ),
    ]
