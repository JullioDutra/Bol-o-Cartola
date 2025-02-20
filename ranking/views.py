# ranking/views.py
from django.shortcuts import render
from selecao.models import Selecao

def ranking(request):
    # Carrega as seleções com os relacionamentos para participantes, torneios, times e o campeão do torneio
    selecao_list = Selecao.objects.select_related(
        'participantes', 'torneios', 'times', 'torneios__campeao'
    )
    
    participants = {}
    for selecao in selecao_list:
        pid = selecao.participantes.id
        if pid not in participants:
            participants[pid] = {
                'nome': selecao.participantes.nome,
                'total_points': 0,
                'selections': []
            }
        participants[pid]['total_points'] += selecao.pontos
        participants[pid]['selections'].append(selecao)
    
    # Ordena os participantes de forma decrescente pelo total de pontos
    ranking_list = sorted(participants.values(), key=lambda x: x['total_points'], reverse=True)
    return render(request, 'ranking.html', {'ranking_list': ranking_list})
