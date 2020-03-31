from django.contrib import admin

from .models import Curso, Avaliacao, AlunoCurso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')


@admin.register(AlunoCurso)
class AlunoCursoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'nome_aluno', 'aluno_idade')

    def nome_curso(self, model):
        return model.curso.titulo

    def nome_aluno(self, model):
        return model.aluno.username

    def aluno_idade(self, model):
        return model.aluno.aluno.age
