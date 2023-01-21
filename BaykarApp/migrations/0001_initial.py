# Generated by Django 4.1.5 on 2023-01-18 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='AirVehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
                ('model_name', models.CharField(max_length=120)),
                ('tail_number', models.CharField(max_length=10)),
                ('iff_code', models.DecimalField(decimal_places=4, max_digits=4)),
                ('weight', models.FloatField(max_length=10)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BaykarApp.category')),
            ],
        ),
    ]
