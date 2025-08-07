from django.urls import path
from .views import (
    DashboardView,
    ListaAlunosView, CriarAlunoView, EditarAlunoView, ExcluirAlunoView,
    ListaCursosView, CriarCursoView, EditarCursoView, ExcluirCursoView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    # Alunos
    path('alunos/', ListaAlunosView.as_view(), name='lista_alunos'),
    path('alunos/novo/', CriarAlunoView.as_view(), name='criar_aluno'),
    path('alunos/<int:pk>/editar/', EditarAlunoView.as_view(), name='editar_aluno'),
    path('alunos/<int:pk>/excluir/', ExcluirAlunoView.as_view(), name='excluir_aluno'),

    # Cursos
    path('cursos/', ListaCursosView.as_view(), name='lista_cursos'),
    path('cursos/novo/', CriarCursoView.as_view(), name='criar_curso'),
    path('cursos/<int:pk>/editar/', EditarCursoView.as_view(), name='editar_curso'),
    path('cursos/<int:pk>/excluir/', ExcluirCursoView.as_view(), name='excluir_curso'),
]
