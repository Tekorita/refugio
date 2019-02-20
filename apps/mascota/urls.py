from django.urls import path, include
#from django.contrib.auth.decorators import login_required

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    path('', index, name='index'),
    #path('nuevo', mascota_view, name='mascota_crear'), #basado en funciones
    path('nuevo', MascotaCreate.as_view(), name='mascota_crear'), #basado en clases
    #path('listar', mascota_list, name='mascota_listar'), #basado en funciones
    path('listar', MascotaList.as_view(), name='mascota_listar'), #basado en clases
    #path('editar/<id_mascota>/', mascota_edit, name='mascota_editar'), #basado en funciones
    path('editar/<pk>/', MascotaUpdate.as_view(), name='mascota_editar'), #basado en clases
    #path('eliminar/<id_mascota>/', mascota_delete, name='mascota_eliminar'), #basado en funciones
    path('eliminar/<pk>/', MascotaDelete.as_view(), name='mascota_eliminar'), #basado en clases
]	