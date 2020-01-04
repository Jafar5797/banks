# Generated by Django 2.2.1 on 2019-09-17 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Banks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='consultants',
            field=models.ManyToManyField(related_name='bankconsultants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bank',
            name='spoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankspoc', to=settings.AUTH_USER_MODEL),
        ),
    ]