# Generated by Django 2.2.5 on 2019-09-19 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0003_auto_20190918_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='Qattachements',
        ),
        migrations.RemoveField(
            model_name='report',
            name='Rattachements',
        ),
    ]
