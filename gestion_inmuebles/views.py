from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegisterForm, UserLoginForm, InmuebleAddForm
from .services import cambiar_datos_usuario, crear_inmueble, verificar_comuna_region, actualizar_inmueble
from .models import Comuna, Region, TipoInmueble, Usuario, Inmueble

# Create your views here.
def index(request):
    return render(request,'index.html',{'title':'Inicio'})

def registro(request):
    if request.method == 'GET':
        context = {
            'form':UserRegisterForm,
            'title':'Registro'
        }
        return render(request, 'register.html', context)

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)        
        if form.is_valid():
            if 'propietario' in request.POST:
                group, created = Group.objects.get_or_create(name='propietario')
            else:
                group, created = Group.objects.get_or_create(name='arrendador')
            user = form.save()
            user.set_password(request.POST['password'])
            user.save()
            user.groups.add(group)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def ingresar(request):
    if request.method == 'GET':
        context = {
            'form':UserLoginForm,
            'title':'Inicio de sesión'
        }
        return render(request,'log_in.html',context)
    if request.method == 'POST':

        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST["password"])
        
        if user is None:
            context = {
                'form':UserLoginForm,
                'title':'Log In',
                'error': f'El usuario {request.POST["username"]} y/o contraseña {request.POST["password"]} son incorrectos'
            }
            return render(request,'log_in.html',context)
        
        else:
            login(request,user)
            return redirect('welcome')
            """
            context = {
                'usuario': user
            }
            welcome(request)
            """
            
        
@login_required
def welcome(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            tipo_usuario = request.user.groups.all()[0].name
            if tipo_usuario == "propietario":
                tipo = 'propietario'
            else:
                tipo = 'arrendador'
            context = {
                'title': 'Bienvenida',
                'usuario': request.user,
                'tipo_usuario': tipo_usuario
            }
            return render(request,'welcome.html',context)
        if request.method == 'POST':              
            if 'search' in request.POST:
                return redirect('search')
            elif 'edit' in request.POST:
                return redirect('edit')
            elif 'add_inmueble' in request.POST:
                return redirect('add_inmueble')
            elif 'edit_inmueble' in request.POST:
                return redirect('show_inmuebles')
            
    else:
        return redirect('ingresar')    

@login_required
def edit(request):
    if request.method == 'GET':
        return render(request,'edit.html',{'title':'Editar Perfil'})
    if request.method == 'POST':
        if request.POST['new_password1']==request.POST['new_password2']:
            user = cambiar_datos_usuario(request.user.username,
                                  request.POST['new_name'],
                                  request.POST['new_lastname'],
                                  request.POST['new_password1'],
                                  request.POST['new_password2'],
                                  request.POST['new_description'])                                  
            login(request,user)
            return redirect(welcome)
        else:
            context = {
                'error':'Las contraseñas no coinciden'
            }
            return render(request,'edit.html',context)
    return render(request,'edit.html')

@login_required
def add_inmueble(request):
    if request.method == 'GET':
        context = {
            'form': InmuebleAddForm,
            'title':'Añadir inmueble'
        }
        return render(request,'add_inmueble.html',context)
    if request.method == 'POST':
        while verificar_comuna_region(id_comuna=request.POST['id_comuna'],id_region=request.POST['id_region']) == False:
            context = {
                'form': InmuebleAddForm,
                'title':'Añadir inmueble',
                'error':'La comuna seleccionada no pertenece a la región.'
            }
            return render(request,'add_inmueble.html',context)
        crear_inmueble(request.POST['nombre'],
                        request.POST['descripcion'],
                        request.POST['m2_construidos'],
                        request.POST['m2_totales'],
                        request.POST['estacionamientos'],
                        request.POST['habitaciones'],
                        request.POST['banos'],
                        request.POST['direccion'],
                        request.POST['precio_mensual'],
                        Region.objects.get(id_region=request.POST['id_region']),
                        Comuna.objects.get(id_comuna=request.POST['id_comuna']),
                        TipoInmueble.objects.get(id_tipo=request.POST['id_tipo']),
                        Usuario.objects.get(id=request.user.id))

        return redirect(welcome) 
    return render(request,'add_inmueble.html',{'title':'Añadir inmueble'})

def show_inmuebles(request):
    inmuebles_de_usuario = Inmueble.objects.filter(id_propietario=request.user.id)
    return render(request,'show_inmuebles.html',{'inmuebles':inmuebles_de_usuario})

@login_required
def edit_inmueble(request,inmueble_id):
    inmueble_to_edit = Inmueble.objects.get(pk=inmueble_id)
    if request.method == 'GET':
        context = {
            'form':InmuebleAddForm(instance=inmueble_to_edit),
            'title':'Editar inmuebles'
        }
        return render(request,'edit_inmueble.html',context)
    else:
        actualizar_inmueble(inmueble_id=inmueble_to_edit.id,kwargs=request.POST)
        return redirect(welcome)
        
@login_required
def delete_inmueble(request, inmueble_id):
    inmueble_del = Inmueble.objects.get(id=inmueble_id)
    inmueble_del.delete()
    return redirect(to='show_inmuebles')

@login_required
def search(request):
    all_inmuebles = Inmueble.objects.all()
    context = {
        'title':'Buscar inmueble',
        'all_inmuebles':all_inmuebles
    }
    return render(request,'search.html',context)


def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'index.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('index')