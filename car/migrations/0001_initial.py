# Generated by Django 3.1 on 2020-08-22 09:01

import django.db.models.deletion
from django.db import migrations, models


def add_statuses(apps, schema_editor):
    db_alias: str = schema_editor.connection.alias
    CarStatus = apps.get_model("car", "CarStatus")
    CarStatus.objects.using(db_alias).bulk_create([
        CarStatus(name="dostępny"),
        CarStatus(name="wypożyczony"),
    ])


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Car Status',
                'verbose_name_plural': 'Car statuses',
            },
        ),
        migrations.RunPython(add_statuses),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=50)),
                ('register_number', models.CharField(max_length=10, unique=True)),
                ('production_year', models.IntegerField(blank=True, null=True)),
                ('status',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='car.carstatus')),
            ],
        ),
    ]
