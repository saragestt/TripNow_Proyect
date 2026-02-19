from django.contrib import admin

from Viajes.models import ImagenReseñas

class ImagenReseñasAdmin(admin.ModelAdmin):
    list_display = ('reseña', 'imagen','creado','actualizado')
    readonly_fields = ('creado', 'actualizado')


admin.site.register(ImagenReseñas,ImagenReseñasAdmin)