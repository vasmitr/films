import datetime

from django.db import models

from films.models import Film


class Day(models.Model):
    DAYS = (
        (1, "Пн"),
        (2, "Вт"),
        (3, "Ср"),
        (4, "Чт"),
        (5, "Пт"),
        (6, "Сб"),
        (7, "Вс")
    )

    number = models.IntegerField(default=1)
    weekend = models.BooleanField(default=False)
    weekend_markup = models.FloatField(default=0.0)

    class Meta:
        ordering = ["number"]
        verbose_name = "День недели"
        verbose_name_plural = "Дни недели"

    def __str__(self):
        for day in self.DAYS:
            if self.number == day[0]:
                return day[1]

    def save(self, *args, **kwargs):
        if self.number in [5, 6, 7]:
            self.weekend = True
            self.weekend_markup = 0.1

        super(Day, self).save(*args, **kwargs)


class Seance(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    film = models.ForeignKey(Film)
    day = models.ForeignKey(Day)
    time_markup = models.FloatField(default=0.0)

    class Meta:
        ordering = ["day", "start", "end"]
        unique_together = ('start', "end", "day")
        verbose_name = "Время сеанса"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s: %s - %s" %(self.day,
            self.start.strftime('%H:%M'),
            self.end.strftime('%H:%M'))

    def save(self, *args, **kwargs):
        if self.start <= datetime.time(12, 0):
            self.time_markup = -0.1
        elif self.start >= datetime.time(17, 0):
            self.time_markup = 0.1

        super(Seance, self).save(*args, **kwargs)
