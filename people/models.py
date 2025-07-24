from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone  # ✅ Import necessário para os defaults

class Curso(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
    
    nome = models.CharField(max_length=200, verbose_name='Nome do Curso')
    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True, verbose_name='Código')
    duracao = models.CharField(max_length=50, default='Indefinida', verbose_name='Duração')
    descricao = models.TextField(default='Descrição temporária', verbose_name='Descrição')
    coordenador = models.CharField(max_length=200, default='Coordenador Temporário', verbose_name='Coordenador')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')
    data_criacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    @property
    def total_alunos(self):
        return self.aluno_set.filter(status='ativo').count()

class Aluno(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('trancado', 'Trancado'),
    ]
    
    phone_regex = RegexValidator(
        regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
        message="Telefone deve estar no formato: '(11) 99999-9999'"
    )
    
    nome = models.CharField(max_length=200, verbose_name='Nome Completo')
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='Email')
    telefone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Telefone')
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='Matrícula')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    # ✅ Aqui está a mudança:
    data_matricula = models.DateField(default=timezone.now, verbose_name='Data de Matrícula')
    data_criacao = models.DateTimeField(default=timezone.now)  # Substitui auto_now_add
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']
    
    def __str__(self):
        return f"{self.nome} - {self.matricula}"
