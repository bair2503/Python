# Generated by Django 3.1 on 2021-02-28 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20210228_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementorder',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='elementorder',
            name='logo_height',
        ),
        migrations.RemoveField(
            model_name='elementorder',
            name='logo_width',
        ),
    ]
