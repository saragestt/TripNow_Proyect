from django.contrib import admin

from Viajes.models import ReseñasModel

class ReseñasAdmin(admin.ModelAdmin):
    list_display = ('identificador','usuario', 'alojamiento', 'slug', 'descripcion', 'puntuacion')
    readonly_fields = ('slug',)



admin.site.register(ReseñasModel,ReseñasAdmin)