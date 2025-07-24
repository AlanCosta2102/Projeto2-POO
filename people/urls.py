from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # URLs para alunos
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('alunos/novo/', views.criar_aluno, name='criar_aluno'),
    path('alunos/<int:pk>/editar/', views.editar_aluno, name='editar_aluno'),
    path('alunos/<int:pk>/excluir/', views.excluir_aluno, name='excluir_aluno'),
    
    # URLs para cursos
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/novo/', views.criar_curso, name='criar_curso'),
    path('cursos/<int:pk>/editar/', views.editar_curso, name='editar_curso'),
    path('cursos/<int:pk>/excluir/', views.excluir_curso, name='excluir_curso'),
]