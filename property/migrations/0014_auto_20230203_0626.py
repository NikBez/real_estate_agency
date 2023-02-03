# Generated by Django 2.2.24 on 2023-02-03 03:26

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20230202_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='phone',
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Номер владельца'),
        ),
    ]
