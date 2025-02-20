# torneios/models.py
from django.db import models

class Torneios(models.Model):
    nome = models.CharField(max_length=100)
    # Campo para definir a sigla manualmente (ex: "mg" para Mineiro)
    sigla = models.CharField(
        max_length=10, 
        blank=True, 
        null=True, 
        help_text="Defina a sigla manualmente (ex: mg para Mineiro)"
    )
    campeao = models.ForeignKey(
        'times.Times', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='championships_won'
    )
    finalistas = models.ManyToManyField(
        'times.Times', 
        blank=True, 
        related_name='finalista_em'
    )
    artilheiro = models.ForeignKey(
        'artilheiros.Artilheiro', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='top_scorer_in'
    )

    def __str__(self):
        return self.nome

    @property
    def sigla_final(self):
        """
        Retorna a sigla definida manualmente ou, se não existir, utiliza os dois primeiros
        caracteres do nome em minúsculo como padrão.
        """
        if self.sigla:
            return self.sigla
        return self.nome[:2].lower()
