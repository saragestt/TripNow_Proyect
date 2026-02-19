from django.contrib import admin

from Viajes.models import AlojamientoModel

class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'nombre_alojamiento', 'fecha_llegada', 'fecha_salida', 'ciudad', 'pais', 'categoria_alojamiento__nombre', 'precio','is_active','creado', 'actualizado')
    list_per_page = 20
    readonly_fields = ('slug','creado', 'actualizado')
    list_editable = ('is_active',)

admin.site.register(AlojamientoModel, AlojamientoAdmin)