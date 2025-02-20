from django.urls import path
from adm.views import admin_resultados, admin_resultados_success

urlpatterns = [
    path('admin-resultados/', admin_resultados, name='admin_resultados'),
    path('sucesso/', admin_resultados_success, name='admin_resultados_success'),
    # ... outras rotas ...
]
