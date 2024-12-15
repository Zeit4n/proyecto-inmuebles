from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Inmueble, Region, Comuna, TipoInmueble

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = ['username','password','confirm_password','email']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mb-3','type':'text'}),
            'password':forms.PasswordInput(attrs={'class':'form-control mb-3','type':'password'}),
            'confirm_password':forms.PasswordInput(attrs={'class':'form-control mb-3','type':'password'}),
            'email':forms.EmailInput(attrs={'class':'form-control mb-3','type':'text'})
        }

        labels = {
            'username':'Nombre de usuario',
            'password': 'Contraseña',
            'confirm_password': 'Confirmar contraseña',
            'email': 'Email'
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = ['username','password']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control mb-3','type':'text'}),
            'password':forms.PasswordInput(attrs={'class':'form-control mb-3','type':'password'}),
        }

        labels = {
            'username':'Nombre de usuario',
            'password': 'Contraseña:'
        }
        
class InmuebleAddForm(forms.ModelForm):
    class Meta:
        model = Inmueble


        fields = ['nombre','id_tipo','descripcion','m2_construidos','m2_totales','estacionamientos','habitaciones','banos','direccion','id_region','id_comuna','precio_mensual']

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control mb-3','type':'text'}),
            'id_tipo':forms.Select(attrs={'class': 'form-control mb-3'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control mb-3','type':'text'}),
            'm2_construidos':forms.NumberInput(attrs={'class':'form-control mb-3','min':0}),
            'm2_totales':forms.NumberInput(attrs={'class':'form-control mb-3','min':0}),
            'estacionamientos':forms.NumberInput(attrs={'class':'form-control mb-3','min':0}),
            'habitaciones':forms.NumberInput(attrs={'class':'form-control mb-3','min':0}),
            'banos':forms.NumberInput(attrs={'class':'form-control mb-3','min':0}),
            'direccion':forms.TextInput(attrs={'class':'form-control mb-3','type':'text'}),
            'id_region':forms.Select(attrs={'class': 'form-control mb-3'}),
            'id_comuna':forms.Select(attrs={'class': 'form-control mb-3'}),
            'precio_mensual':forms.NumberInput(attrs={'class':'form-control mb-3','min':0})
        }

        label = {
            'nombre':'Nombre de inmueble',
            'id_tipo':'Tipo de inmueble',
            'descripcion':'Descripción de inmueble',
            'm2_construidos':'Metros cuadrados construidos',
            'm2_totales':'Metros cuadrados totales',
            'estacionamientos':'Número de estacionamientos',
            'habitaciones':'Número de habitaciones',
            'banos':'Número de baños',
            'direccion':'Dirección',
            'id_region':'Región',
            'id_comuna':'Comuna',
            'precio_mensual':'Precio (mensual)'
        }
        id_tipo = forms.ModelChoiceField(queryset=TipoInmueble.objects.all(), required=True)
        id_region = forms.ModelChoiceField(queryset=Region.objects.all(), required=True)
        id_comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), required=True)


        