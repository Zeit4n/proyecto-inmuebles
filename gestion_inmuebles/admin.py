from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Inmueble, Region, Comuna, TipoInmueble, Usuario
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('id','username')

class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion','m2_construidos','m2_totales','estacionamientos','habitaciones','banos','direccion','precio_mensual','eliminada','id_comuna','id_region','id_tipo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('precio_mensual', 'id_comuna')

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id_region','nombre')
    search_fields = ['nombre']
    list_filter = ['id_region']

class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre')

class TipoInmuebleAdmin(admin.ModelAdmin):
    list_display = ('tipo_inmueble')
    
admin.site.register(Inmueble,InmuebleAdmin)
admin.site.register(Usuario,CustomUserAdmin)
admin.site.register(Region)
admin.site.register(Comuna,ComunaAdmin)
admin.site.register(TipoInmueble)
