from django.contrib import admin
from Users.models import Preferencias


class PreferenciasAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_per_page = 20

admin.site.register(Preferencias, PreferenciasAdmin)