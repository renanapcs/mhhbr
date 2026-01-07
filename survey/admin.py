from django.contrib import admin
from .models import HipHopSurvey


@admin.register(HipHopSurvey)
class HipHopSurveyAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'pseudonimo', 'atuacao', 'municipio', 
        'estado', 'idade', 'genero', 'cor', 'criado_em'
    ]
    list_filter = [
        'atuacao', 'estado', 'genero', 'cor', 'formado', 'criado_em'
    ]
    search_fields = [
        'nome', 'pseudonimo', 'municipio', 'estado', 'nome_grupo'
    ]
    readonly_fields = ['criado_em', 'atualizado_em']
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('user', 'nome', 'pseudonimo')
        }),
        ('Localização', {
            'fields': ('estado', 'municipio')
        }),
        ('Demografia', {
            'fields': ('idade', 'cor', 'genero')
        }),
        ('Atuação no Hip-Hop', {
            'fields': (
                'atuacao', 'tempo_hiphop', 'nome_grupo', 
                'membros_masculinos', 'membros_femininos'
            )
        }),
        ('Formação', {
            'fields': ('formado', 'qual_formacao')
        }),
        ('Informações Adicionais', {
            'fields': ('observacoes',)
        }),
        ('Metadados', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )

