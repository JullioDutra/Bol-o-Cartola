from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from torneios.models import Torneios
from times.models import Times
from artilheiros.models import Artilheiro
from adm.forms import AdminResultadosForm
from selecao.models import calcular_pontos_para_campeonato

@staff_member_required
def admin_resultados(request):
    if request.method == 'POST':
        form = AdminResultadosForm(request.POST)
        if form.is_valid():
            torneios = Torneios.objects.all()
            for torn in torneios:
                champ_field_name = f'champ_{torn.id}'
                finalists_field_name = f'finalists_{torn.id}'
                art_field_name = f'art_{torn.id}'

                champ_id = form.cleaned_data[champ_field_name]
                finalist_ids = form.cleaned_data[finalists_field_name]
                art_id = form.cleaned_data[art_field_name]

                # Atualiza os dados do torneio:
                torn.campeao = Times.objects.get(id=int(champ_id))
                torn.artilheiro = Artilheiro.objects.get(id=int(art_id))
                torn.save()
                # Atualiza o ManyToMany de finalistas:
                torn.finalistas.set([Times.objects.get(id=int(team_id)) for team_id in finalist_ids])
                torn.save()
                # Recalcula os pontos para este torneio
                calcular_pontos_para_campeonato(torn)
            return redirect('admin_resultados_success')  # Redireciona para uma página de sucesso
    else:
        form = AdminResultadosForm()
    return render(request, 'admin_resultados.html', {'form': form})

def admin_resultados_success(request):
    return render(request, 'admin_resultados_success.html')