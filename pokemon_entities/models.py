from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(blank=True, null=True)
    description = models.TextField()


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='покемон',
        related_name='entities')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appear_at = models.DateTimeField(verbose_name='дата и время появления')
    disappear_at = models.DateTimeField(blank=True,
                                        null=True,
                                        verbose_name='дата и время исчезновения')
    level = models.IntegerField(default=1, verbose_name="Уровень")
    health = models.IntegerField(default=1, verbose_name="Здоровье")
    strength = models.IntegerField(default=1, verbose_name="Атака")
    defence = models.IntegerField(default=1, verbose_name="Защита")
    stamina = models.IntegerField(default=1, verbose_name="Выносливость")