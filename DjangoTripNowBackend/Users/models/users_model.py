import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.db import models



class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Correo no valido')
        if "@" not in email:
            raise ValueError('Formato de correo válido')

        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise ValueError(
                f"Formatos no permitidos: " + ", ".join(
                    settings.EXTENSIONES_BLACKLIST))

        if not password:
            raise ValueError("Contraseña no válida")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)  #si lo pongo aqui (mira abajo)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    info_personal = models.ForeignKey('InfoModel', on_delete=models.CASCADE, null=True, blank=True)
    prefer_personal = models.ManyToManyField('Preferencias', verbose_name='Preferencias')
    paises = models.ManyToManyField('PaisesModel', verbose_name='Paises')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' #para preguntar con que campo se identifica
    REQUIRED_FIELDS = []  #lo pongo tambien aqui :)

    def __str__(self):
        full_name = f"{self.nombre} {self.apellidos}"
        return full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            provisional = uuid.uuid4().hex
            while CustomUser.objects.filter(slug=provisional).exists():
                provisional = uuid.uuid4().hex

            self.slug = provisional
        return super().save(*args, **kwargs)



    class Meta:
        db_table = 'Usuarios'
        ordering = ['-is_superuser', 'is_active', 'nombre']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'