from django.db import models
from django.contrib.auth.models import User

from films.models import Film
from seances.models import Seance


class Seat(models.Model):
    number = models.IntegerField()
    seance = models.ForeignKey(Seance)
    row_markup = models.FloatField(default=0.0)
    reserved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('number', 'seance')
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        if self.number in range(1, 11):
            self.row_markup = 0.2
        elif self.number in range(11, 31):
            self.row_markup = 0.1
        elif self.number in range(71, 101):
            self.row_markup = -0.1

        super(Seat, self).save(*args, **kwargs)


class Ticket(models.Model):
    owner = models.ForeignKey(User)
    seat = models.ManyToManyField(Seat)
    seance = models.ForeignKey(Seance)
    film = models.ForeignKey(Film)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"

    def __str__(self):
        return "Билет № %d" % self.id

    def count_price(self):
        pass
    
    def reserve(self):
        pass
