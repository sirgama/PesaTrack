# Generated by Django 4.0.5 on 2022-06-23 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_name_profile_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='income',
            field=models.IntegerField(default=0),
        ),
    ]
