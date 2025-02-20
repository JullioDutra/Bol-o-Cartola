from django.db import models
from participante.models import Participantes
from torneios.models import Torneios
from times.models import Times
from artilheiros.models import Artilheiro




class Selecao(models.Model):
    participantes = models.ForeignKey(Participantes, on_delete=models.CASCADE, related_name='predictions')
    torneios = models.ForeignKey(Torneios, on_delete=models.CASCADE)
    times = models.ForeignKey(Times, on_delete=models.CASCADE)
    custom = models.BooleanField(default=False)  # True se o time foi adicionado via "Outro? Qual?"
    # Novo campo para artilheiro:
    artilheiro = models.ForeignKey(Artilheiro, null=True, blank=True, on_delete=models.CASCADE, related_name='predictions_art')
    pontos = models.IntegerField(default=0)

    class Meta:
        unique_together = ('participantes', 'torneios')

    def __str__(self):
        return f"{self.participantes} - {self.torneios}: {self.times} | Artilheiro: {self.artilheiro}"

    
    

def calcular_pontos_para_campeonato(torn):
    for selecao in Selecao.objects.filter(torneios=torn):
        pts = 0
        # Pontos para o campeão:
        if torn.campeao and selecao.times == torn.campeao:
            pts += (100 if selecao.custom else 50)
        # Pontos para finalistas:
        elif torn.finalistas.filter(id=selecao.times.id).exists():
            pts += 20
        # Pontos para o artilheiro:
        if torn.artilheiro and selecao.artilheiro == torn.artilheiro:
            pts += 150
        selecao.pontos = pts
        selecao.save()


