from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Users.models import CustomUser,InfoModel


class InfoPersonalInLine(admin.StackedInline):
    model = InfoModel
    can_delete = False
    verbose_name = 'Informacion personal'
    verbose_name_plural = 'Datos personales'

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'nombre', 'apellidos', 'is_active', 'info_personal')
    list_per_page = 20
    list_editable = ('is_active',)

    ordering = ('email',)


admin.site.register(CustomUser,CustomUserAdmin)