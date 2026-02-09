from django.db import models

class PaisesModel(models.Model):
    pais = models.CharField(max_length=100,)

    class Meta:
        db_table = 'paises'
        verbose_name = 'pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.pais