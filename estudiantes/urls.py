from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alumnx, name='lista_alumnx'),
    path('estudiantes/nuevo/', views.alumnx_nuevo, name='alumnx_nuevo'),
    path('estudiantes/editar/<int:pk>', views.alumnx_edit, name='alumnx_edit'),
    path('estudiantes/eliminar/<int:pk>', views.eliminar_alumnx, name='eliminar_alumnx'),
    path('estudiantes/listacalif1erparcial/', views.lista_calif1erpar, name='lista_calif1erpar'),
    path('estudiantes/1erparcial/', views.primer_parcial, name='primer_parcial'),
    path('estudiantes/editar_1er_parcial/<int:pk>/', views.primer_parcial_edit, name='primer_parcial_edit'),
]
