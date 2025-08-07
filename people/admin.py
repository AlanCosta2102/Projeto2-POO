from django.contrib import admin
from .models import Aluno, Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'matricula', 'status')
    search_fields = ('nome', 'email', 'matricula')
    list_filter = ('status',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'coordenador')
    search_fields = ('nome', 'codigo', 'coordenador')
