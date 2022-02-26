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
    path('estudiantes/listacalif2doparcial/', views.lista_calif2dopar, name='lista_calif2dopar'),
    path('estudiantes/2doparcial/', views.segundo_parcial, name='segundo_parcial'),
    path('estudiantes/editar_2do_parcial/<int:pk>/', views.segundo_parcial_edit, name='segundo_parcial_edit'),
    path('estudiantes/listacalif_final_parcial/', views.lista_calif_final, name='lista_calif_final'),
    path('estudiantes/final_parcial/', views.final_parcial, name='final_parcial'),
    path('estudiantes/editar_final_parcial/<int:pk>/', views.final_parcial_edit, name='final_parcial_edit'),
    path('estudiantes/lista_autobiografia/', views.lista_autobiografia, name='lista_autobiografia'),
    path('estudiantes/autobiografia/', views.autobiografia, name='autobiografia'),
    path('estudiantes/editar_autobiografia/<int:pk>/', views.autobiografia_edit, name='autobiografia_edit'),
]
