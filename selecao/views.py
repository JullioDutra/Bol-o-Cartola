# views.py
from django.shortcuts import render, redirect, get_object_or_404
from participante.models import Participantes
from torneios.models import Torneios
from times.models import Times
from .forms import SelecaoForm
from .models import Selecao
from artilheiros.models import Artilheiro

def showcartolandia(request):
    if request.method == 'POST':
        form = SelecaoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            participantes, created = Participantes.objects.get_or_create(nome=nome)
            
            for torn in Torneios.objects.all():
                # Processamento da seleção do time:
                field_key = f"torn_{torn.id}"
                custom_field_key = f"torn_custom_{torn.id}"
                value = form.cleaned_data.get(field_key)
                if value == 'other':
                    custom_team_nome = form.cleaned_data.get(custom_field_key)
                    if custom_team_nome:
                        team, created_team = Times.objects.get_or_create(
                            torneios=torn,
                            nome__iexact=custom_team_nome,
                            defaults={'nome': custom_team_nome}
                        )
                        custom = True
                    else:
                        continue
                else:
                    team = get_object_or_404(Times, id=int(value))
                    custom = False

                # Processamento da seleção do artilheiro:
                art_field_key = f"art_{torn.id}"
                art_custom_field_key = f"art_custom_{torn.id}"
                art_value = form.cleaned_data.get(art_field_key)
                if art_value == 'other':
                    art_custom_nome = form.cleaned_data.get(art_custom_field_key)
                    if art_custom_nome:
                        # Cria o artilheiro vinculando-o ao torneio atual
                        artilheiro, created_art = Artilheiro.objects.get_or_create(
                            nome__iexact=art_custom_nome,
                            torneio=torn,
                            defaults={'nome': art_custom_nome}
                        )
                    else:
                        continue
                else:
                    # Garante que o artilheiro pertence ao torneio atual
                    artilheiro = get_object_or_404(Artilheiro, id=int(art_value), torneio=torn)
                
                # Salva ou atualiza a previsão (Selecao) para esse torneio, incluindo o artilheiro
                Selecao.objects.update_or_create(
                    participantes=participantes,
                    torneios=torn,
                    defaults={'times': team, 'custom': custom, 'artilheiro': artilheiro}
                )
            return redirect('thank_you')
    else:
        form = SelecaoForm()
    
    # Passa os torneios para o template, se necessário
    torneios = Torneios.objects.all()
    return render(request, 'selecao.html', {'form': form, 'torneios': torneios})

def obrigado(request):
    return render(request, 'obrigado.html')
