import csv
import os
from django.core.management.base import BaseCommand
from torneios.models import Torneios
from times.models import Times

class Command(BaseCommand):
    help = 'Importa times e campeonatos de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **kwargs):
        csv_path = kwargs['csv_file']

        if not os.path.exists(csv_path):
            self.stdout.write(self.style.ERROR(f"Arquivo {csv_path} não encontrado."))
            return

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 2:
                    self.stdout.write(self.style.WARNING(f"Linha inválida: {row}"))
                    continue

                torneio_nome, time_nome = row
                torneio, _ = Torneios.objects.get_or_create(nome=torneio_nome)
                time, _ = Times.objects.get_or_create(nome=time_nome, torneios=torneio)

                self.stdout.write(self.style.SUCCESS(f"Time '{time_nome}' adicionado ao torneio '{torneio_nome}'."))

        self.stdout.write(self.style.SUCCESS("Importação concluída."))
