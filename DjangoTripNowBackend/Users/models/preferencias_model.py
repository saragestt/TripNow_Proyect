from django.db import models


class Preferencias(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        db_table = 'preferencias'
        verbose_name = 'preferencia'
        verbose_name_plural = 'preferencias'


    def __str__(self):
        return self.nombre