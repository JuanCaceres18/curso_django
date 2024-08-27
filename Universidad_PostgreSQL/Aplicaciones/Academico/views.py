from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Curso

# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    # Traigo los 5 primeros registros.
    # cursosListados = Curso.objects.all()[:5]
    # Se toma en cuenta el segundo criterio (créditos) si los nombres del registro son iguales.
    # cursosListados = Curso.objects.all().order_by("nombre", "creditos")
    # cursosListados = Curso.objects.filter(nombre="Python", creditos=100)
    
    # Mostrar los que tienen créditos mayores a 4.
    # cursosListados = Curso.objects.filter(creditos__gte=4)
    
    # Mostrar los que tienen créditos menores a 4
    # cursosListados = Curso.objects.filter(creditos__lte=6)

    # Mostrar los que empiezan por X letra
    # cursosListados = Curso.objects.filter(nombre__startswith="P")

    # Mostrar los que contienen X letra
    # cursosListados = Curso.objects.filter(nombre__contains="t")


    # return HttpResponse("<h1>Hola mundo</h1>")
    data = {
        "titulo":"Gestion de cursos",
        "cursos": cursosListados
    }
    # return render(request, "gestion_cursos.html", {"cursos": cursosListados})
    return render(request, "gestion_cursos.html", data)

class CursoListView(ListView):
    model = Curso
    template_name = "gestion_cursos.html"

    def get_queryset(self):
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Gestión de Cursos"
        print(context)
        return context

def registrar_curso(request):
    nombre = request.POST["txtNombre"]
    creditos = request.POST["numCreditos"]

    curso = Curso.objects.create(nombre=nombre, creditos=creditos)

    return redirect("/")

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect("/")
