# Generated by Django 3.2.4 on 2021-07-05 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
