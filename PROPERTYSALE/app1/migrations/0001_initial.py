# Generated by Django 2.2.4 on 2019-10-31 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appartment',
            fields=[
                ('apartname', models.CharField(max_length=40)),
                ('apartno', models.IntegerField(primary_key='True', serialize=False)),
                ('noofplats', models.IntegerField()),
                ('costofplat', models.FloatField()),
                ('noofvacant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NewPlot',
            fields=[
                ('plotno', models.IntegerField(primary_key=True, serialize=False)),
                ('roadnumber', models.IntegerField()),
                ('surveyno', models.IntegerField()),
                ('costsqare', models.IntegerField()),
                ('otherexpences', models.IntegerField()),
                ('boundaries', models.IntegerField()),
                ('facing', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('totalcost', models.IntegerField()),
            ],
        ),
    ]
