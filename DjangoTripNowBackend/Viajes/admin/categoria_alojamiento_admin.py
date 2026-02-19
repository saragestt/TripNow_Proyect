from django.contrib import admin

from Viajes.models import CategoriaAlojamiento

class CategoriaAlojamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'creado', 'modificado')
    readonly_fields = ('slug', 'creado', 'modificado')

admin.site.register(CategoriaAlojamiento, CategoriaAlojamientoAdmin)