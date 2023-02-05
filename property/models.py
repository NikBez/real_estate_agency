from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    new_building = models.BooleanField("Новостройка", null=True)
    likes = models.ManyToManyField(User, blank=True, related_name="flat_likes")


    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

class Complaint(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="complaints")
    flat = models.ForeignKey(Flat, verbose_name="Квартира", on_delete=models.CASCADE, related_name="complaints")
    text = models.TextField("Текст жалобы", max_length=500)

class Owner(models.Model):
    name = models.CharField("ФИО", max_length=100, db_index=True)
    pure_phone = PhoneNumberField("Номер владельца", blank=True)
    flats = models.ManyToManyField(Flat, verbose_name="Квартиры в собственности", blank=True, related_name="own_by")

    def __str__(self):
        return f"{self.name} - {self.pure_phone}"
