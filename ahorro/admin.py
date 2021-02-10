from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import Profile, Color, Plazo, Ahorro, Sistema, PrePlazo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Color)

@admin.register(Plazo)
class PLazoAdmin(admin.ModelAdmin):
    list_display = ('frecuencia', 'tiempo', 'meta', 'sistema')
    readonly_fields = ('id',)
# admin.site.register(Plazo, ShowID)

class AhorroAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'sistema', 'fecha', 'id')
admin.site.register(Ahorro, AhorroAdmin)

admin.site.register(PrePlazo)

@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'user', 'meta', 'url', 'image', 'created', 'id']
    list_filter = ['created']



