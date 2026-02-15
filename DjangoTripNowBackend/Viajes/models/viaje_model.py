from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify




class Viaje(models.Model):

    identificador = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name="Identificador")
    ciudad_salida = models.CharField(max_length=100, unique=False, blank=False, null=False, verbose_name="Ciudad salida")
    ciudad_llegada = models.CharField(max_length=100, unique=False, blank=False, null=False, verbose_name="Ciudad llegada")

    terminal_salida = models.CharField(max_length=100, unique=False, blank=False, null=False, verbose_name="Terminal salida")
    terminal_llegada = models.CharField(max_length=100, unique=False, blank=False, null=False, verbose_name="Terminal llegada")


    lugar_salida = models.CharField(max_length=100, blank=False, null=False, verbose_name="Lugar salida")
    lugar_llegada = models.CharField(max_length=100, blank=False, null=False, verbose_name="Lugar llegada")

    fecha_salida = models.DateField(blank=False, null=False, verbose_name="Fecha de salida ida")
    fecha_llegada = models.DateField(blank=False, null=False, verbose_name="Fecha de llegada ida")

    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, verbose_name="Precio")

    categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Categoria")

    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True, verbose_name="Slug")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        db_table = 'Viajes'
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"
        ordering = ['-categoria__nombre', '-identificador']

    def __str__(self):
        return f":{self.identificador} / {self.ciudad_salida} - {self.ciudad_llegada} / {self.terminal_salida} - {self.terminal_llegada} / {self.lugar_salida} - {self.lugar_llegada} / {self.fecha_salida} - {self.fecha_llegada} / {self.precio} / {self.categoria.nombre}"

    def save (self, *args, **kwargs):
        if not self.slug:
            prov = slugify(self.identificador)
            cont = 1

            while Viaje.objects.filter(slug=prov).exists():
                prov = slugify(self.identificador) + str(cont)
                cont = cont + 1
            self.slug = prov

            viaje = Viaje.objects.filter(identificador=self.identificador).first()
            if viaje and viaje.id != self.id:
                raise ValidationError("El viaje ya existe en la base de datos")
            super().save(*args, **kwargs)