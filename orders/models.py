from django.db import models

class Order(models.Model):
    client = models.CharField(max_length=255, verbose_name='Фио')
    insta = models.CharField(max_length=50, verbose_name='Инстаграм')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    address = models.CharField(max_length=300, null=True, blank=True, verbose_name='Адрес')
    model = models.CharField(max_length=100, verbose_name='Модель')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    amount = models.IntegerField(verbose_name='Количество')
    size = models.CharField(max_length=50, verbose_name='Размер')
    articul = models.CharField(max_length=255, verbose_name='Артикул')
    price = models.IntegerField(verbose_name='Цена')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    pending = models.BooleanField(default=False)
    in_transit = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    completed =models.BooleanField(default=False)

    def __str__(self):
        return self.client

