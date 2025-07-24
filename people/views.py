from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, Count
from django.core.paginator import Paginator
from .models import Aluno, Curso
from .forms import AlunoForm, CursoForm

def dashboard(request):
    # Estatísticas gerais
    total_alunos = Aluno.objects.filter(status='ativo').count()
    total_cursos = Curso.objects.filter(status='ativo').count()
    total_matriculas = Aluno.objects.count()
    
    # Alunos recentes
    alunos_recentes = Aluno.objects.order_by('-data_criacao')[:5]
    
    # Cursos com mais alunos
    cursos_populares = Curso.objects.annotate(
        num_alunos=Count('aluno')
    ).order_by('-num_alunos')[:5]
    
    context = {
        'total_alunos': total_alunos,
        'total_cursos': total_cursos,
        'total_matriculas': total_matriculas,
        'alunos_recentes': alunos_recentes,
        'cursos_populares': cursos_populares,
    }
    return render(request, 'core/dashboard.html', context)

def lista_alunos(request):
    busca = request.GET.get('busca', '')
    status_filtro = request.GET.get('status', '')
    
    alunos = Aluno.objects.all()
    
    if busca:
        alunos = alunos.filter(
            Q(nome__icontains=busca) |
            Q(email__icontains=busca) |
            Q(matricula__icontains=busca)
        )
    
    if status_filtro:
        alunos = alunos.filter(status=status_filtro)
    
    alunos = alunos.order_by('nome')
    
    paginator = Paginator(alunos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'busca': busca,
        'status_filtro': status_filtro,
    }
    return render(request, 'core/lista_alunos.html', context)

def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    
    return render(request, 'core/form_aluno.html', {'form': form, 'titulo': 'Cadastrar Aluno'})

def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno atualizado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    
    return render(request, 'core/form_aluno.html', {'form': form, 'titulo': 'Editar Aluno'})

def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    
    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Aluno excluído com sucesso!')
        return redirect('lista_alunos')
    
    return render(request, 'core/confirmar_exclusao.html', {'objeto': aluno, 'tipo': 'aluno'})

def lista_cursos(request):
    busca = request.GET.get('busca', '')
    
    cursos = Curso.objects.all()
    
    if busca:
        cursos = cursos.filter(
            Q(nome__icontains=busca) |
            Q(codigo__icontains=busca) |
            Q(coordenador__icontains=busca)
        )
    
    cursos = cursos.annotate(num_alunos=Count('aluno')).order_by('nome')
    
    paginator = Paginator(cursos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'busca': busca,
    }
    return render(request, 'core/lista_cursos.html', context)

def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso cadastrado com sucesso!')
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    
    return render(request, 'core/form_curso.html', {'form': form, 'titulo': 'Cadastrar Curso'})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso atualizado com sucesso!')
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    
    return render(request, 'core/form_curso.html', {'form': form, 'titulo': 'Editar Curso'})

def excluir_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso excluído com sucesso!')
        return redirect('lista_cursos')
    
    return render(request, 'core/confirmar_exclusao.html', {'objeto': curso, 'tipo': 'curso'})