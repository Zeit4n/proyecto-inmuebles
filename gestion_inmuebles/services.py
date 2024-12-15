import json
from .models import Inmueble,Comuna,Region,Usuario,TipoInmueble 
#from django.contrib.auth.models import User

def crear_inmueble(nombre,descripcion,m2_construidos,m2_totales,estacionamientos,habitaciones,banos,direccion,precio_mensual,region,comuna,tipo_inmueble,id_usuario):
    inmueble = Inmueble(nombre=nombre,descripcion=descripcion,m2_construidos=m2_construidos,
    m2_totales=m2_totales,estacionamientos=estacionamientos,habitaciones=habitaciones,
    banos=banos,direccion=direccion,precio_mensual=precio_mensual,id_region=region,id_comuna=comuna,id_tipo=tipo_inmueble,id_propietario=id_usuario)
    inmueble.save()
    return inmueble

def eliminar_inmueble(inmueble_id):
    inmueble = Inmueble.objects.get(pk=inmueble_id)
    inmueble.eliminada = True
    inmueble.save()
    return mostrar_inmuebles()

def actualizar_inmueble(inmueble_id,**kwargs):
    inmueble = Inmueble.objects.get(pk=inmueble_id)
    for key, value in kwargs['kwargs'].items():
        if key == 'csrfmiddlewaretoken':
            pass
        elif value.isnumeric() == True:
            if key == 'id_tipo':    
                setattr(inmueble,key,TipoInmueble.objects.get(pk=int(value)))
            elif key == 'id_region':    
                setattr(inmueble,key,Region.objects.get(pk=int(value)))
            elif key == 'id_comuna':    
                setattr(inmueble,key,Comuna.objects.get(pk=int(value)))
            else:
                setattr(inmueble,key,int(value))
        else:
            setattr(inmueble,key,value)
    inmueble.save()
    return inmueble
    #return kwargs.get()[0]

def mostrar_inmuebles():
    inmuebles = Inmueble.objects.exclude(eliminada=True)
    return inmuebles

def separar_inmuebles():
    inmuebles = Inmueble.objects.filter
    pass

def exportar_inmuebles_comuna():
    comunas = Inmueble.objects.values_list('id_comuna_id', flat=True).distinct()
    with open("inmuebles_comuna.txt","w",encoding='utf-8') as file:        
        for i in comunas:
            inmuebles_comuna = Inmueble.objects.filter(id_comuna_id=i)
            for j in range(len(inmuebles_comuna)):
                instancia_inmueble = {
                    "comuna":Comuna.objects.get(id_comuna=i).nombre,
                    "nombre":inmuebles_comuna[j].nombre,
                    "descripcion":inmuebles_comuna[j].descripcion,
                }
                row = json.dumps(instancia_inmueble,ensure_ascii=False)
                file.write(row)
                file.write('\n')
    file.close()

def exportar_inmuebles_region():
    regiones = Inmueble.objects.values_list('id_region_id', flat=True).distinct()
    with open("inmuebles_region.txt","w",encoding='utf-8') as file:        
        for i in regiones:
            inmuebles_region = Inmueble.objects.filter(id_region_id=i)
            for j in range(len(inmuebles_region)):
                instancia_inmueble = {
                    "region":Region.objects.get(id_region=i).nombre,
                    "nombre":inmuebles_region[j].nombre,
                    "descripcion":inmuebles_region[j].descripcion,
                    "m2_construidos":inmuebles_region[j].m2_construidos,
                    "m2_totales":inmuebles_region[j].m2_totales,
                    "estacionamientos":inmuebles_region[j].estacionamientos,
                    "habitaciones":inmuebles_region[j].habitaciones,
                    "baños":inmuebles_region[j].banos,
                    "direccion":inmuebles_region[j].direccion,
                    "precio_mensual":float(inmuebles_region[j].precio_mensual),
                    "eliminada":inmuebles_region[j].eliminada,
                }
                row = json.dumps(instancia_inmueble,ensure_ascii=False)
                file.write(row)
                file.write('\n')
    file.close()

def cambiar_datos_usuario(name, new_name, new_lastname, new_password, confirm_password, new_description):
    usuario = Usuario.objects.get(username=name)
    usuario.first_name = new_name
    usuario.last_name = new_lastname
    usuario.set_password(new_password)
    usuario.confirm_password = confirm_password
    usuario.description = new_description
    #usuario.img_profile = new_img
    usuario.save()
    return usuario

def verificar_comuna_region(id_comuna, id_region):
    id_comunas = Comuna.objects.filter(id_region=id_region)
    if int(id_comuna) in id_comunas.values_list('id_comuna',flat=True):
        return True
    else:
        return False

#Puede copiar y pegar las siguientes líneas de código en la shell de django para probar el código

#from gestion_inmuebles.services import * (desde \proyectos_inmuebles)
#crear_inmueble('lala','chico',6,15,2,4,2,'Lalola','Macul','Lal',1500)
#crear_inmueble('lolo','grande',5,16,4,78,9,'Luli','La Florida','Lel',2000)
#mostrar_inmuebles()
#eliminar_inmueble(0)

#Si añade nuevos inmuebles tenga en cuenta que la clave primaria de Inmueble es un Serial, por lo que
#si desea eliminar un inmueble tenga en cuenta esto para obtener el id del inmueble.

