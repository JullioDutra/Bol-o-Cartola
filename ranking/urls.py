from django.urls import path
from .views import ranking


urlpatterns = [
    path('ranking/', ranking, name='ranking'),
    # ... outras rotas ...
]
