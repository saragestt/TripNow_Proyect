from django.contrib import admin

from Viajes.models import ImagenViaje

class ImagenViajeAdmin(admin.ModelAdmin):
    list_display = ('viaje__identificador', 'imagen', 'creado', 'actualizado')
    readonly_fields = ('creado', 'actualizado')

admin.site.register(ImagenViaje,ImagenViajeAdmin)