from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class ReseñasModel(models.Model):
    identificador = models.CharField(max_length=100, unique=True, verbose_name="Identificador", blank=False, null=False)
    usuario = models.ForeignKey("Users.CustomUser", on_delete=models.CASCADE, blank=False, null=False, verbose_name="Usuario")
    alojamiento = models.ForeignKey("AlojamientoModel",on_delete=models.CASCADE, blank=False, null=False, verbose_name="Alojamiento")
    slug = models.SlugField(blank=False, null=False, verbose_name="Slug", unique=True)
    descripcion = models.TextField(blank=False, null=False, verbose_name="Descripcion")
    puntuacion = models.PositiveIntegerField(blank=False, null=False, verbose_name="Puntuacion", default=0, choices=[(i,i) for i in range(0,6)])


    class Meta:
        db_table = "Reseñas"
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return f"{self.identificador} - {self.usuario} -{self.alojamiento}- {self.puntuacion}"

    def save (self, *args, **kwargs):
        if not self.slug:
            prov = slugify(self.identificador)
            cont = 1

            while ReseñasModel.objects.filter(identificador=prov).exists():
                prov = slugify(self.identificador) + " - " + str(cont)
                cont = cont + 1

            self.slug = prov

        reseña = ReseñasModel.objects.filter(identificador=self.identificador).first()
        if reseña and reseña.id != self.id:
            raise ValidationError("Ya se ha creado una reseña anteriormente")
        super().save(*args, **kwargs)

