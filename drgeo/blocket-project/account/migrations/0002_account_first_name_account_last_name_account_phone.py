# Generated by Django 4.1.dev20211026075023 on 2021-10-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(default='', max_length=30),
        ),
    ]