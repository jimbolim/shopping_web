# Generated by Django 2.0 on 2018-08-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='img_url',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='goods'),
        ),
    ]
