from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    
class Film(models.Model):

    STARS = (
        (0, "Нет оценки"),
        (1, "Плохо"),
        (2, "Сойдет"),
        (3, "Средне"),
        (4, "Неплохо"),
        (5, "Круто")
    )
    
    name = models.CharField(max_length=200)
    rating = models.IntegerField(choices=STARS, default=0)
    image = models.ImageField()
    base_price = models.IntegerField()
    relise_date = models.DateField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["rating"]
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.name

