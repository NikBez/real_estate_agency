# Generated by Django 2.2.24 on 2023-02-02 09:19

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields

import phonenumbers


def fill_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        parset_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_possible_number(parset_phone) and phonenumbers.is_valid_number(parset_phone):
            flat.owner_pure_phone = phonenumbers.format_number(parset_phone, phonenumbers.PhoneNumberFormat.E164)
        else:
            flat.owner_pure_phone = ""
        flat.save()



def move_backward(apps, schema_editor):
    Flat = apps.get_models("property", "Flat")
    flats = Flat.objects.all()
    for flat in flats.iterator():
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.RunPython(fill_phone_numbers, move_backward)
    ]
