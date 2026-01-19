from django.contrib import admin
from .models import Patient

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    # Campos que aparecem na lista
    list_display = (
        'name',
        'CPF',
        'gender',
        'admission_date',
        'phone'
    )

    # Campo clicável
    list_display_links = ('name', 'CPF',)

    # Busca no topo
    search_fields = ('name', 'CPF',)

    # Filtros laterais
    list_filter = ('gender','admission_date',)

    # Ordenação padrão
    ordering = ('name',)

    # Quantos registros por página
    list_per_page = 20


