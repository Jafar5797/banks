# Generated by Django 2.2.5 on 2019-09-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='name',
            field=models.CharField(default='cps', max_length=50),
            preserve_default=False,
        ),
    ]
