# Generated by Django 2.1.3 on 2018-12-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20181201_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
