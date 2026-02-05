from django.contrib import admin
from Users.models import InfoModel

class CategoryAdmin(admin.ModelAdmin): #Esto lo pone bonito y lo ordena
    list_display = ('direccion','telefono', 'fecha_nacimiento', 'nacionalidad', 'pasaporte') #para que se vea en este orden la tabla
    list_per_page = 20
    list_editable = ('telefono',)

admin.site.register(InfoModel,CategoryAdmin)