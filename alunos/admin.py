from django.contrib import admin

from django.contrib import admin

from .models import Aluno


@admin.register(Aluno)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('username', 'age')

    def username(self, x):
        return x.user.username
