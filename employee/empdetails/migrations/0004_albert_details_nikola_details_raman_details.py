# Generated by Django 4.1.4 on 2022-12-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empdetails', '0003_nikola_raman_rename_scientist_albert'),
    ]

    operations = [
        migrations.AddField(
            model_name='albert',
            name='details',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='nikola',
            name='details',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='raman',
            name='details',
            field=models.TextField(default=0),
        ),
    ]
