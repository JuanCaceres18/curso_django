from django.contrib import admin
from .models import Curso, Docente

# Nueva forma de registrar
@admin.register(Curso)
class cursoAdmin(admin.ModelAdmin):
    list_display = ("id", "datos", "creditos")
    # Ordenar campos
    # ordering = ("nombre", "creditos")
    # Establecer una barra de búsqueda
    # search_fields = ("nombre", "creditos")
    # Indicar que los campos son editables
    # list_editable = ("nombre", "creditos")
    # Crear hipervínculos
    # list_display_links = ("nombre",)
    # # Filtrar
    # list_filter = ("creditos",)
    # # Cantidad de registros por página
    # list_per_page = 3
    # # Inidicar cuáles campos no son editables
    # exclude = ("creditos",)

    # Opciones avanzadas 
    """
    fieldsets = (
        (None, {
            'fields':('nombre',)
        }),
        ('Avanced options', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('creditos',)
        })
    )
    """
    def datos(self,obj):
        return obj.nombre.upper()
    
    # Cambiar nombre de columna
    datos.short_description = "CURSO MAYUS"
    # Si tengo un valor vacío muestro "???"
    datos.empty_value_display = "???"
    datos.admin_order_field = "nombre"

# admin.site.register(Curso, cursoAdmin)
admin.site.register(Docente)