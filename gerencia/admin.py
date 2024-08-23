from django.contrib import admin
from.models import *
from django.utils.html import format_html

# Register your models here.
@admin.register(Aluno)
class AlunoAdmin (admin.ModelAdmin):
    list_display = ['nome','email','data_nascimento',]