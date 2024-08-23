from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    imagem = models.ImageField(upload_to='imagens_salvas/', null=True, blank=True)

    def __str__(self):
        return self.nome
