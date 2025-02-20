from django.db import models

class Times(models.Model):
    torneios = models.ForeignKey('torneios.Torneios', on_delete=models.CASCADE, related_name='times')
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='times_fotos/', null=True, blank=True)  # Novo campo de foto

    def __str__(self):
        return f"{self.nome} ({self.torneios.nome})"


