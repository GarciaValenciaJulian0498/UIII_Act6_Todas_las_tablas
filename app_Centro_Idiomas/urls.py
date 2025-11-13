from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_centro_idiomas, name='inicio_centro_idiomas'),
    path('idiomas/agregar/', views.agregar_idioma, name='agregar_idioma'),
    path('idiomas/', views.ver_idiomas, name='ver_idiomas'),
    path('idiomas/actualizar/<int:id_idioma>/', views.actualizar_idioma, name='actualizar_idioma'),
    path('idiomas/borrar/<int:id_idioma>/', views.borrar_idioma, name='borrar_idioma'),
    
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/', views.ver_profesores, name='ver_profesores'),
    path('profesores/actualizar/<int:pk>/', views.actualizar_profesor, name='actualizar_profesor'),
    path('profesores/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_profesor, name='realizar_actualizacion_profesor'),
    path('profesores/borrar/<int:pk>/', views.borrar_profesor, name='borrar_profesor'),

    path('clases/agregar/', views.agregar_clase, name='agregar_clase'),
    path('clases/', views.ver_clases, name='ver_clases'),
    path('clases/actualizar/<int:pk>/', views.actualizar_clase, name='actualizar_clase'),
    path('clases/actualizar_post/<int:pk>/', views.realizar_actualizacion_clase, name='realizar_actualizacion_clase'),
    path('clases/borrar/<int:pk>/', views.borrar_clase, name='borrar_clase'),

    path('alumnos/agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('alumnos/', views.ver_alumnos, name='ver_alumnos'),
    path('alumnos/actualizar/<int:pk>/', views.actualizar_alumno, name='actualizar_alumno'),
    path('alumnos/actualizar/submit/<int:pk>/', views.realizar_actualizacion_alumno, name='realizar_actualizacion_alumno'),
    path('alumnos/borrar/<int:pk>/', views.borrar_alumno, name='borrar_alumno'),

    # URLs para Aulas
    path('aulas/agregar/', views.agregar_aula, name='agregar_aula'),
    path('aulas/', views.ver_aulas, name='ver_aulas'),
    path('aulas/actualizar/<int:pk>/', views.actualizar_aula, name='actualizar_aula'),
    path('aulas/actualizar/submit/<int:pk>/', views.realizar_actualizacion_aula, name='realizar_actualizacion_aula'),
    path('aulas/borrar/<int:pk>/', views.borrar_aula, name='borrar_aula'),
]