# forms.py
from django import forms
from participante.models import Participantes
from torneios.models import Torneios
from times.models import Times
from artilheiros.models import Artilheiro

class SelecaoForm(forms.Form):
    nome = forms.CharField(label="Seu nome", max_length=100)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        torneios = Torneios.objects.all().order_by('nome')
        for torn in torneios:
            # Campos para seleção do time:
            choices = [(str(times.id), times.nome) for times in torn.times.all()]
            choices.append(('other', 'Outro? Qual?'))
            self.fields[f"torn_{torn.id}"] = forms.ChoiceField(
                label=torn.nome,
                choices=choices,
                widget=forms.RadioSelect
            )
            self.fields[f"torn_custom_{torn.id}"] = forms.CharField(
                label="Se 'Outro', qual?",
                required=False
            )
            # Campos para seleção do artilheiro, filtrando pelos artilheiros vinculados a esse torneio
            art_choices = [(str(art.id), art.nome) for art in torn.artilheiros.all()]
            art_choices.append(('other', 'Outro? Qual?'))
            self.fields[f"art_{torn.id}"] = forms.ChoiceField(
                label=f"Artilheiro - {torn.nome}",
                choices=art_choices,
                widget=forms.RadioSelect
            )
            self.fields[f"art_custom_{torn.id}"] = forms.CharField(
                label="Se 'Outro', qual?",
                required=False
            )
