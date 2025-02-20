# artilheiros/models.py
from django.db import models

class Artilheiro(models.Model):
    nome = models.CharField(max_length=100)
    # Relaciona o artilheiro a um torneio específico
    torneio = models.ForeignKey(
        'torneios.Torneios',
        on_delete=models.CASCADE,
        related_name='artilheiros'
    )

    def __str__(self):
        return self.nome
