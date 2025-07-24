from django import forms
from .models import Aluno, Curso

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'telefone', 'matricula', 'curso', 'status', 'data_matricula']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome completo do aluno'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@exemplo.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(11) 99999-9999'
            }),
            'matricula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2024001'
            }),
            'curso': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'data_matricula': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'codigo', 'duracao', 'descricao', 'coordenador', 'status']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do curso'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CC001'
            }),
            'duracao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '8 semestres'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descrição do curso...'
            }),
            'coordenador': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prof. Dr. João Silva'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }