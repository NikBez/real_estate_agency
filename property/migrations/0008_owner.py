# Generated by Django 2.2.24 on 2023-02-02 09:59

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20230202_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Номер владельца')),
                ('pure_phone', models.CharField(blank=True, max_length=15, verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(blank=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
