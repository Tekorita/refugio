from django.urls import path, include



from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
	path('index', index_adopcion, name='index'),
    path('listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('editar/<pk>', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('eliminar/<pk>', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]