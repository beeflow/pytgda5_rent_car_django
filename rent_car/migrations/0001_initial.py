# Generated by Django 3.1 on 2020-08-22 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0003_auto_20200822_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_time', models.DateTimeField(null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
