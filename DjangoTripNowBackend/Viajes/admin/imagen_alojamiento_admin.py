from django.contrib import admin

from Viajes.models import ImagenAlojamiento

class ImagenAlojamientoAdmin(admin.ModelAdmin):
    list_display = ('alojamiento__identificador', 'imagen', 'creado', 'actualizado')
    readonly_fields = ('creado', 'actualizado')

admin.site.register(ImagenAlojamiento, ImagenAlojamientoAdmin)
