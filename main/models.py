from django.db import models


class TableReservation(models.Model):
    name = models.CharField('Имя', max_length=20)
    tableNumber = models.IntegerField('Номер столика')
    reservationTime = models.TimeField('Время')
    email = models.EmailField('Почта', default='mail@mail.ru')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Бронрование'
        verbose_name_plural = 'Забронированные столы'


