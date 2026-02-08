from django.db import models

class InfoModel(models.Model):
    direccion = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    fecha_nacimiento = models.DateField(max_length=10, blank=False, null=False)
    nacionalidad = models.CharField(max_length=30, blank=False, null=False)
    pasaporte = models.CharField(max_length=30, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)



    def __str__(self):
        return f"{self.telefono} - {self.fecha_nacimiento} - {self.nacionalidad} - {self.direccion} - {self.pasaporte} - {self.codigo_postal}"

    class Meta:
        db_table = 'Informacion Personal'
        verbose_name = 'Informacion Personal'
        verbose_name_plural = 'Datos Personales'

