# Generated by Django 2.0 on 2018-08-28 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20180828_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='care_instructions_and_other_details',
            new_name='other_details',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='content',
        ),
    ]