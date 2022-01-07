from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alumnx, name='lista_alumnx'),
        path('estudiantes/nuevo/', views.alumnx_nuevo, name='alumnx_nuevo'),
]
