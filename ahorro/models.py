import datetime
from django.urls import reverse
from django.db.models import F

from django.utils import timezone 

from django.db import models
from django.utils import timezone

from .example import sistema_Ahorro
from .example import Lista_total
from .example import cantidadFija


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






######################################
#
#           CANTIDAD FIJA
#
##########################################

class CantidadFija(models.Model):
    nombre = models.CharField(max_length=200)
    not_archived = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='systemF_created',
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


    def my_cantidad(self):
        "cantidad es igual a meta entre tiempo"
        return cantidadFija(int(self.frecuencia), int(self.tiempo), int(self.meta))    

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super(CantidadFija, self).save(*args, **kwargs)
    
    def get_absolute_url(self): 
        return reverse('ahorro:fijoSystem',
                        args=[self.id,])

    def absolute_url(self):
        return reverse('ahorro:sistemaDetalle',
                        args=[self.id,])

    def archived_url(self):
        return reverse('ahorro:userArchivedF',
                        args=[self.id,])                    



#####################################################
#
#             LA META ES AHORRAR MODEL
#
#####################################################




class AhorrarEsLaMeta(models.Model):
    '''
    Solo tendra la opción de poner su ahorro cada vez que quiera ahorrar
    si meta sin limite de tiempo sin periodicidad 
    deberia tener opcion de periodicidad si quiere que le aviden chido si no pues no
    si es si el usuario escoge cada cuanto, creo que no sobra.
    va
    entonces el decide cuanto ahorrar no tiene meta simplemente es un control de sus ahorros
    si asi lo desea el usuario recibirá un aviso para ahorrar
    
    '''
    nombre = models.CharField(max_length=200)
    not_archived = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='systemAM_created',
                            on_delete=models.CASCADE)


    # el usuario elige FRECUENCIA
    ZERO = '0'
    DIARIO = '1'
    QUINCENAL = '15'
    MENSUAL = '30'

    FRECUENCIA = [
        (ZERO, _('Ahorraré cuando pueda/quiera')),
        (DIARIO, _('Todos los días')),
        (QUINCENAL, _('Cada quince días')),
        (MENSUAL, _('Al mes')),
    ]

    frecuencia = models.CharField(max_length=200,
                                  choices=FRECUENCIA,
                                  default=ZERO,
                                  )                        


    # cantidad = models.IntegerField()

    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    # def my_cantidad(self):
    #     "cantidad es igual a meta entre tiempo"
    #     return cantidadFija(int(self.frecuencia), int(self.tiempo), int(self.meta))    

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super(AhorrarEsLaMeta, self).save(*args, **kwargs)
    
    def get_absolute_url(self): 
        return reverse('ahorro:MetaAhorrarSystem',
                        args=[self.id,])

    def absolute_url(self):
        return reverse('ahorro:sistemaDetalle',
                        args=[self.id,])

    def archived_url(self):
        return reverse('ahorro:userArchivedAM',
                        args=[self.id,])         



##########################################
#
#          END LA META ES AHORRAR MODEL
#
##########################################




##################################################
#
#         EN DONDE SE GUARDAN LOS AHORROS
#
###############################################



class Ahorro(models.Model):
    cantidad = models.IntegerField(validators=[MinValueValidator(10, message="Vamos, a que puedes ahorrar mas de 10 pesos")])
    # meta = models.IntegerField(validators=[MinValueValidator(1825, message="Ahorra a partir de 2000")])
    fecha = models.DateTimeField(default = timezone.now)
    sistema = models.ForeignKey(Sistema, related_name = 'ahorros', on_delete=models.CASCADE, null=True, blank=True)
    sistemaF = models.ForeignKey(CantidadFija, related_name = 'ahorrosF', on_delete=models.CASCADE, null=True, blank=True)
    sistemaAM = models.ForeignKey(AhorrarEsLaMeta, related_name = 'ahorrosAM', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.cantidad)        
    








# class SinLimiteDeTiempo(models.Model):
#     nombre = models.CharField(max_length=200)
#     not_archived = models.BooleanField(default=True)
#     slug = models.SlugField(max_length=200, blank=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                             related_name='system_created',
#                             on_delete=models.CASCADE)
#     # plazo = models.ForeignKey(Plazo, on_delete=models.CASCADE)
#     # PLAZO INCLUIDO
#     ##############

#     DIARIO = '1'
#     QUINCENAL = '15'
#     MENSUAL = '30'

#     FRECUENCIA = [
#         (DIARIO, _('Todos los días')),
#         (QUINCENAL, _('Cada quince días')),
#         (MENSUAL, _('Al mes')),
#     ]

#     frecuencia = models.CharField(max_length=200,
#                                   choices=FRECUENCIA,
#                                   default=MENSUAL,
#                                   )

 
#     meta = models.IntegerField(validators=[MinValueValidator(1825, message="Ahorra a partir de 2000")])

#     cantidad = models.IntegerField()

#     description = models.TextField(blank=True)
#     url = models.URLField(blank=True)
#     image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
#     created = models.DateField(auto_now_add=True, db_index=True)



    
#     def my_list(self):
#         "retorna la division de frecuencia y tiempo"
#         return sistema_Ahorro(int(self.frecuencia), int(self.tiempo), int(self.meta))

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

#     def archived_url(self):
#         return reverse('ahorro:userArchived',
#                         args=[self.id,])                    







# class LibreSinLimiteDeTiempo(models.Model):
#     nombre = models.CharField(max_length=200)
#     not_archived = models.BooleanField(default=True)
#     slug = models.SlugField(max_length=200, blank=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                             related_name='system_created',
#                             on_delete=models.CASCADE)
#     # plazo = models.ForeignKey(Plazo, on_delete=models.CASCADE)
#     # PLAZO INCLUIDO
#     ##############

#     DIARIO = '1'
#     QUINCENAL = '15'
#     MENSUAL = '30'

#     FRECUENCIA = [
#         (DIARIO, _('Todos los días')),
#         (QUINCENAL, _('Cada quince días')),
#         (MENSUAL, _('Al mes')),
#     ]

#     frecuencia = models.CharField(max_length=200,
#                                   choices=FRECUENCIA,
#                                   default=MENSUAL,
#                                   )

 
#     meta = models.IntegerField(validators=[MinValueValidator(1825, message="Ahorra a partir de 2000")])

#     cantidad = models.IntegerField()

#     description = models.TextField(blank=True)
#     url = models.URLField(blank=True)
#     image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
#     created = models.DateField(auto_now_add=True, db_index=True)



    
#     def my_list(self):
#         "retorna la division de frecuencia y tiempo"
#         return sistema_Ahorro(int(self.frecuencia), int(self.tiempo), int(self.meta))

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

#     def archived_url(self):
#         return reverse('ahorro:userArchived',
#                         args=[self.id,])                    






    
#     def my_list(self):
#         "retorna la division de frecuencia y tiempo"
#         return sistema_Ahorro(int(self.frecuencia), int(self.tiempo), int(self.meta))

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

#     def archived_url(self):
#         return reverse('ahorro:userArchived',
#                         args=[self.id,])                    


