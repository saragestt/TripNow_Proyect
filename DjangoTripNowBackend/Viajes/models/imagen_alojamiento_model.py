from django.db import models

class ImagenAlojamiento(models.Model):
    alojamiento = models.OneToOneField("AlojamientoModel", on_delete=models.CASCADE, related_name="imagen")
    imagen = models.ImageField(upload_to="images/", verbose_name="Imagen", blank=False, null=False)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        db_table = "imagen_alojamiento"
        verbose_name = "Imagen alojamiento"
        verbose_name_plural = "Imagenes alojamientos"


    def __str__(self):
        return f"Imagen alojamiento: {self.alojamiento.identificador}"

    def save(self, *args, **kwargs):
        if self.imagen:
            nombre_imagen = self.alojamiento.slug
            extension_imagen = self.imagen.name.split(".")[-1]
            self.imagen.name = f"{nombre_imagen}.{extension_imagen}"
        super().save(*args, **kwargs)
