# Generated by Django 3.1 on 2021-03-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210311_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='logo'),
        ),
    ]
