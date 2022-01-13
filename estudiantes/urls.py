from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alumnx, name='lista_alumnx'),
    path('estudiantes/nuevo/', views.alumnx_nuevo, name='alumnx_nuevo'),
    path('estudiantes/editar/<int:pk>', views.alumnx_edit, name='alumnx_edit'),
    path('estudiantes/eliminar/<int:pk>', views.eliminar_alumnx, name='eliminar_alumnx'),
]
