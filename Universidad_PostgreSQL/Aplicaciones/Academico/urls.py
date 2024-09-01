from django.urls import path

from Aplicaciones.Academico.views import CursoListView, eliminar_curso, registrar_curso, leer_curso

# Rutas
urlpatterns = [
    # Con as_view lo transformo en vista.
    path('', CursoListView.as_view(), name='gestionCursos'),
    path('registrarCurso/', registrar_curso),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('edicionCurso/<int:id>', leer_curso)
]