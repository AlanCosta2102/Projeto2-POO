from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Aluno, Curso
from .forms import AlunoForm, CursoForm
from .mixins import TitleMixin

from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

# Aluno

@method_decorator(login_required, name='dispatch')
class ListaAlunosView(TitleMixin, ListView):
    model = Aluno
    template_name = 'core/lista_alunos.html'
    context_object_name = 'page_obj'
    paginate_by = 10
    title = 'Lista de Alunos'

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('busca', '')
        status = self.request.GET.get('status', '')
        if busca:
            queryset = queryset.filter(
                Q(nome__icontains=busca) |
                Q(email__icontains=busca) |
                Q(matricula__icontains=busca)
            )
        if status:
            queryset = queryset.filter(status=status)
        return queryset.order_by('nome')

@method_decorator(login_required, name='dispatch')
class CriarAlunoView(TitleMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'core/form_aluno.html'
    success_url = reverse_lazy('lista_alunos')
    title = 'Cadastrar Aluno'

    def form_valid(self, form):
        messages.success(self.request, 'Aluno cadastrado com sucesso!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditarAlunoView(TitleMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'core/form_aluno.html'
    success_url = reverse_lazy('lista_alunos')
    title = 'Editar Aluno'

    def form_valid(self, form):
        messages.success(self.request, 'Aluno atualizado com sucesso!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ExcluirAlunoView(DeleteView):
    model = Aluno
    template_name = 'core/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_alunos')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Aluno excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'aluno'
        context['objeto'] = self.object
        return context

# Curso

@method_decorator(login_required, name='dispatch')
class ListaCursosView(TitleMixin, ListView):
    model = Curso
    template_name = 'core/lista_cursos.html'
    context_object_name = 'page_obj'
    paginate_by = 9
    title = 'Lista de Cursos'

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('busca', '')
        if busca:
            queryset = queryset.filter(
                Q(nome__icontains=busca) |
                Q(codigo__icontains=busca) |
                Q(coordenador__icontains=busca)
            )
        return queryset.annotate(num_alunos=Count('aluno')).order_by('nome')

@method_decorator(login_required, name='dispatch')
class CriarCursoView(TitleMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'core/form_curso.html'
    success_url = reverse_lazy('lista_cursos')
    title = 'Cadastrar Curso'

    def form_valid(self, form):
        messages.success(self.request, 'Curso cadastrado com sucesso!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditarCursoView(TitleMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'core/form_curso.html'
    success_url = reverse_lazy('lista_cursos')
    title = 'Editar Curso'

    def form_valid(self, form):
        messages.success(self.request, 'Curso atualizado com sucesso!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ExcluirCursoView(DeleteView):
    model = Curso
    template_name = 'core/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_cursos')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Curso excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo'] = 'curso'
        context['objeto'] = self.object
        return context
