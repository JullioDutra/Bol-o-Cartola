from django.contrib import admin
from torneios.models import Torneios
from times.models import Times
from .models import Selecao
from artilheiros.models import Artilheiro

admin.site.register(Times)
admin.site.register(Torneios)
admin.site.register(Selecao)
admin.site.register(Artilheiro)
