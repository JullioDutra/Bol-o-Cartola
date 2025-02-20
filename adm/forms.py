from django import forms
from torneios.models import Torneios
from times.models import Times
from artilheiros.models import Artilheiro

class AdminResultadosForm(forms.Form):
    """
    Formulário dinâmico que, para cada torneio, adiciona campos:
      - campeao (ChoiceField)
      - finalists (MultipleChoiceField)
      - artilheiro (ChoiceField)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        torneios = Torneios.objects.all().order_by('nome')
        for torn in torneios:
            # Campeão: escolhas baseadas nos times deste torneio
            champ_choices = [(team.id, team.nome) for team in torn.times.all()]
            champ_field_name = f'champ_{torn.id}'
            self.fields[champ_field_name] = forms.ChoiceField(
                label=f"Campeão - {torn.nome}",
                choices=champ_choices,
                required=True
            )
            
            # Finalistas: múltipla escolha (pode ser vazio)
            finalist_choices = [(team.id, team.nome) for team in torn.times.all()]
            finalist_field_name = f'finalists_{torn.id}'
            self.fields[finalist_field_name] = forms.MultipleChoiceField(
                label=f"Finalistas - {torn.nome}",
                choices=finalist_choices,
                required=False,
                widget=forms.CheckboxSelectMultiple
            )
            
            # Artilheiro: escolhas baseadas no modelo Artilheiro
            art_choices = [(art.id, art.nome) for art in Artilheiro.objects.all()]
            art_field_name = f'art_{torn.id}'
            self.fields[art_field_name] = forms.ChoiceField(
                label=f"Artilheiro - {torn.nome}",
                choices=art_choices,
                required=True
            )
