# Generated by Django 2.2.5 on 2019-09-19 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0006_auto_20190919_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='queryfiles',
        ),
        migrations.RemoveField(
            model_name='report',
            name='responsefiles',
        ),
    ]