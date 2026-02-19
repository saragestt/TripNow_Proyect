from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class AlojamientoModel(models.Model):

    identificador = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name="identificador")
    nombre_alojamiento = models.CharField(unique=True, max_length=50, blank=False, null=False, verbose_name="Nombre del alojamiento")
    fecha_llegada= models.DateField(null=False, blank=False, verbose_name="Fecha llegada")
    fecha_salida = models.DateField(null=False, blank=False, verbose_name="Fecha salida")
    ciudad = models.CharField( max_length=50, blank=False, null=False, verbose_name="Ciudad")
    pais = models.CharField( max_length=50, blank=False, null=False, verbose_name="Pais")
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Precio")

    categoria_alojamiento = models.ForeignKey("CategoriaAlojamiento", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Categoria alojamiento")

    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False, verbose_name="slug")

    is_active = models.BooleanField(default=True, verbose_name="Activo")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")


    class Meta:
        db_table = 'Alojamientos'
        verbose_name = 'Alojamiento'
        verbose_name_plural = 'Alojamientos'
        ordering = ['-identificador']

    def __str__(self):
        return f"{self.nombre_alojamiento}"

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = slugify(self.identificador)
            cont = 1

            while AlojamientoModel.objects.filter(slug=prov).exists():
                prov = slugify(self.identificador) + str(cont)
                cont = cont + 1
            self.slug = prov


            alojamiento = AlojamientoModel.objects.filter(identificador=self.identificador).first()
            if alojamiento and alojamiento.id != self.id:
                raise ValidationError("El alojamiento ya existe")
            super().save(*args, **kwargs)

