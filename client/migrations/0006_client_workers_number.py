# Generated by Django 5.0 on 2023-12-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_clientfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='workers_number',
            field=models.IntegerField(default=0),
        ),
    ]
