# Generated by Django 3.2.9 on 2023-01-19 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BaykarApp', '0002_auto_20230119_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airvehicle',
            name='updated_date',
        ),
    ]
