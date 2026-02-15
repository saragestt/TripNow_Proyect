from django.db import models

class ImagenViaje(models.Model):
    viaje = models.OneToOneField("Viaje", on_delete=models.CASCADE, related_name="imagen")
    imagen = models.ImageField(upload_to="images/", verbose_name="Imagen", blank=False, null=False)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        db_table = "imagen_viaje"
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"


    def __str__(self):
        return f"Imagen viaje: {self.viaje.identificador}"

    def save(self, *args, **kwargs):
        if self.imagen:
            nombre_imagen = self.viaje.slug
            extension_imagen = self.imagen.name.split(".")[-1]
            self.imagen.name = f"{nombre_imagen}.{extension_imagen}"
        super().save(*args, **kwargs)
