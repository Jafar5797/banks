# Generated by Django 2.2.5 on 2019-09-20 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0008_auto_20190919_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='q_report',
            name='requests_recieved',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='report',
            name='topic',
            field=models.TextField(),
        ),
    ]
