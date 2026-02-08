from django.db import models

class PreferenciasChoices(models.TextChoices):
    VIAJE = "VIAJE EN CARRETERA"
    CINE = "CINE"
    FOTO = "FOTOGRAFIA"
    ESPIRITUALIDAD = "ESPIRITUALIDAD"
    ARTE = "ARTE"
    SALUD = "SALUD MENTAL"
    JUEGOS = "JUEGOS MESA"
    VIDEOJUEGO = "VIDEOJUEGOS"
    ACAMPADA = "ACAMPADA"
    CRUELTY = "CRUELTY FREE"
    QUEDAR = "QUEDAR CON AMIGOS"
    VOLUNTARIADO = "VOLUNTARIADO"
    LGBTQ = "LGBTQ+"



class Preferencias(models.Model):

    preferencia = models.CharField(choices=PreferenciasChoices.choices,null=False,blank=False,max_length=20, verbose_name='Preferencia 1')
    preferencia_dos = models.CharField(choices=PreferenciasChoices.choices, null=False, blank=False, max_length=20, verbose_name='Preferencia 2')
    preferencia_tres = models.CharField(choices=PreferenciasChoices.choices, null=False, blank=False, max_length=20, verbose_name='Preferencia 3')
    preferencia_cuatro = models.CharField(choices=PreferenciasChoices.choices, null=False, blank=False, max_length=20, verbose_name='Preferencia 4')
    preferencia_cinco = models.CharField(choices=PreferenciasChoices.choices, null=False, blank=False, max_length=20, verbose_name='Preferencia 5',default='viaje')

    class Meta:
        db_table = 'preferencias'
        verbose_name = 'preferencia'
        verbose_name_plural = 'preferencias'


    def __str__(self):
        return self.preferencia