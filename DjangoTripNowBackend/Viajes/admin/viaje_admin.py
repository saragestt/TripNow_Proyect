from django.contrib import admin

from Viajes.models import Viaje

class ViajeAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'ciudad_salida', 'ciudad_llegada', 'terminal_salida', 'terminal_llegada', 'lugar_salida', 'lugar_llegada', 'fecha_salida', 'fecha_llegada', 'precio', 'categoria__nombre','is_active','creado', 'actualizado')
    list_per_page = 20
    readonly_fields = ('slug','creado', 'actualizado')
    list_editable = ('is_active', )

admin.site.register(Viaje,ViajeAdmin)