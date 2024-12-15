"""
URL configuration for proyecto_inmuebles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from gestion_inmuebles import views as gestion_inmuebles_views
urlpatterns = [
    #path('signup/', gestion_inmuebles_views.register, name='register'),
    path('signup/', gestion_inmuebles_views.registro, name='register'),
    path('contact/', gestion_inmuebles_views.contact, name='contact'),
    path('login/', gestion_inmuebles_views.ingresar, name='log_in'),
    path('welcome/', gestion_inmuebles_views.welcome, name='welcome'),
    path('edit/',gestion_inmuebles_views.edit,name='edit'),
    path('search/',gestion_inmuebles_views.search,name='search'),
    path('add_inmueble/',gestion_inmuebles_views.add_inmueble,name='add_inmueble'),
    path('edit_inmueble/<int:inmueble_id>/',gestion_inmuebles_views.edit_inmueble,name='edit_inmueble'),    
    path('<int:inmueble_id>/delete', gestion_inmuebles_views.delete_inmueble, name='delete_inmueble'),
    path('show_inmueble/',gestion_inmuebles_views.show_inmuebles,name='show_inmuebles'),
    path('logout/',gestion_inmuebles_views.log_out,name='log_out'),
    path('admin/', admin.site.urls),
    path('', gestion_inmuebles_views.index,name='index'),
]