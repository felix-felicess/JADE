from django.db import models
from contas.models import Usuario  # para associar tarefa a um usuário

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('concluida', 'Concluída')],
        default='pendente'
    )
    data_limite = models.DateField(null=True, blank=True)
    data_entrega = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return self.titulo
