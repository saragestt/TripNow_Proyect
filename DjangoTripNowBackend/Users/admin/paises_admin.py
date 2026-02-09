from django.contrib import admin
from Users.models import PaisesModel

class PaisesAdmin(admin.ModelAdmin):
    list_display = ('pais',)
    list_per_page = 20


admin.site.register(PaisesModel, PaisesAdmin)