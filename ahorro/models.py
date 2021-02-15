import datetime
from django.urls import reverse
from django.db.models import F

from django.utils import timezone 

from django.db import models
from django.utils import timezone

from .example import sistema_Ahorro
from .example import Lista_total


from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator


from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings # new
# from django.contrib.auth.models import User # new

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
import re 
# from .managers import CustomUserManager

# Create your models here.


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.EmailField(max_length=200)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     nombre = models.CharField(max_length=200)
#     USERNAME_FIELD = 'email'
#     # USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username) 

class Color(models.Model):
    HEX = models.CharField(max_length=7)
    def __str__(self):
        return self.HEX





# class Sistema(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                             related_name='system_created',
#                             on_delete=models.CASCADE)
#     nombre = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, blank=True)
#     # plazo = models.ForeignKey(Plazo, on_delete=models.CASCADE)
#     description = models.TextField(blank=True)
#     url = models.URLField(blank=True)
#     image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
#     created = models.DateField(auto_now_add=True, db_index=True)
#     users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
#                                         related_name='images_liked',
#                                         blank=True)
#     total_likes = models.PositiveIntegerField(db_index=True, default=0)

#     def __str__(self):
#         return self.nombre

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.nombre)
#         super(Sistema, self).save(*args, **kwargs)
    
#     def get_absolute_url(self): 
#         return reverse('ahorro:userSystem',
#                         args=[self.id,])

#     def absolute_url(self):
#         return reverse('ahorro:sistemaDetalle',
#                         args=[self.id,])




# SISTEMA TEST CON PLAZO INCLUIDO


# def validate_number(value):
#     if value == int:
#         raise ValidationError(('Usa solo números'), params={'value': value},)



# validate_number = RegexValidator(regex='\D', message="Usa únicamente números")

class Sistema(models.Model):
    nombre = models.CharField(max_length=200)
    not_archived = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='system_created',
                            on_delete=models.CASCADE)
    # plazo = models.ForeignKey(Plazo, on_delete=models.CASCADE)
    # PLAZO INCLUIDO
    ##############

    DIARIO = '1'
    QUINCENAL = '15'
    MENSUAL = '30'

    FRECUENCIA = [
        (DIARIO, _('Todos los días')),
        (QUINCENAL, _('Cada quince días')),
        (MENSUAL, _('Al mes')),
    ]

    frecuencia = models.CharField(max_length=200,
                                  choices=FRECUENCIA,
                                  default=MENSUAL,
                                  )

    SEISMESES = '183'
    UNANO = '365'
    DOSANOS = '730'
    CINCOANOS = '1825'

    TIEMPO = [
        (SEISMESES, _('Medio año')),
        (UNANO, _('Un año')),
        (DOSANOS, _('Dos años')),
        (CINCOANOS, _('Cinco años')),
    ]

    tiempo = models.CharField(max_length=200,
                              choices=TIEMPO,
                              default=UNANO)
 
    meta = models.IntegerField(validators=[MinValueValidator(1825, message="Ahorra a partir de 2000")])

    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)



    
    def my_list(self):
        "retorna la division de frecuencia y tiempo"
        return sistema_Ahorro(int(self.frecuencia), int(self.tiempo), int(self.meta))

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super(Sistema, self).save(*args, **kwargs)
    
    def get_absolute_url(self): 
        return reverse('ahorro:userSystem',
                        args=[self.id,])

    def absolute_url(self):
        return reverse('ahorro:sistemaDetalle',
                        args=[self.id,])

    def archived_url(self):
        return reverse('ahorro:userArchived',
                        args=[self.id,])                    










class Plazo(models.Model):
    DIARIO = '1'
    QUINCENAL = '15'
    MENSUAL = '30'

    FRECUENCIA = [
        (DIARIO, _('Todos los días')),
        (QUINCENAL, _('Cada quince días')),
        (MENSUAL, _('Al mes')),
    ]

    frecuencia = models.CharField(max_length=200,
                                  choices=FRECUENCIA,
                                  default=MENSUAL,
                                  )

    SEISMESES = '183'
    UNANO = '365'
    DOSANOS = '730'
    CINCOANOS = '1825'

    TIEMPO = [
        (SEISMESES, _('Medio año')),
        (UNANO, _('Un año')),
        (DOSANOS, _('Dos años')),
        (CINCOANOS, _('Cinco años')),
    ]

    tiempo = models.CharField(max_length=200,
                              choices=TIEMPO,
                              default=UNANO)
 
    meta = models.CharField(max_length=200)
    sistema = models.ForeignKey(Sistema, related_name = 'sistema', on_delete=models.CASCADE)
 
    def my_list(self):
        "retorna la division de frecuencia y tiempo"
        # return int(self.frecuencia) * int(self.tiempo)
        return sistema_Ahorro(int(self.frecuencia), int(self.tiempo), int(self.meta))
    # def absolute_url(self):
    #     return reverse('ahorro:ahorroDetalle',
    #                     args=[self.id,])    
    def __str__(self):
        return self.meta
    






class Ahorro(models.Model):
    cantidad = models.CharField(max_length=200)
    fecha = models.DateTimeField(default = timezone.now)
    sistema = models.ForeignKey(Sistema, related_name = 'ahorros', on_delete=models.CASCADE)
    def __str__(self):
        return self.cantidad        
    



class PrePlazo(models.Model):
    '''
    
    - nombre del sistema
    - descripcion del sistema
    - url al formulario del sistema

    '''
    nombre = models.CharField(max_length=200)
    tiempo = models.CharField(max_length=200)
    frecuencia = models.CharField(max_length=200)
    meta = models.CharField(max_length=200)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre





#  # paste in your models.py
# def only_int(value): 
#     if value.isdigit()==False:
#         raise ValidationError('Usa solo números')