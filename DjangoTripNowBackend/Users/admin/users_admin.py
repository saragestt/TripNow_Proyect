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
    
    fieldsets = [
        ('Información personal', {
            'fields': [
                'email', 'nombre', 'apellidos', 'is_active', 'info_personal', 'prefer_personal', 'paises'
            ],
        }),
    ]

    add_fieldsets = (
        ("Información personal", {
            'classes': ('wide',),
            'fields': ('nombre', 'apellidos', 'info_personal', 'prefer_personal', 'paises')}
         ),
        ("Información de iniciar sesión", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
        ("Configuración", {
            'classes': ('wide',),
            'fields': ('is_active', 'is_staff', 'is_superuser',)}
         ),
    )


admin.site.register(CustomUser,CustomUserAdmin)