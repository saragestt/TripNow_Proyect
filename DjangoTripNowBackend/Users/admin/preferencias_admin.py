from django.contrib import admin
from Users.models import Preferencias


class PreferenciasAdmin(admin.ModelAdmin):
    list_display = ('preferencia', 'preferencia_dos', 'preferencia_tres', 'preferencia_cuatro', 'preferencia_cinco')
    list_per_page = 20

admin.site.register(Preferencias, PreferenciasAdmin)