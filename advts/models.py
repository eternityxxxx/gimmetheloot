from django.db import models


class Advert(models.Model):

    title = models.CharField(max_length=128, verbose_name='Заголовок объявления')
    description = models.TextField(verbose_name='Текст объявления')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')
    address = models.CharField(max_length=128, verbose_name='Адрес')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и вермя создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего обновления')

    def __str__(self):
        return self.title + ' ' + str(self.price)
