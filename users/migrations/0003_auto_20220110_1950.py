# Generated by Django 3.2.4 on 2022-01-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='highest_degree',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]
