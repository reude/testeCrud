from django.urls import path, include
from django.contrib import admin
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    path('', include('app_cad_usuarios.urls')),
]
