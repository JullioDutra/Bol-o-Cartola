
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('selecao.urls')),
    path('adm/', include('adm.urls')),
    path('cartolandia/', include('ranking.urls')),
]
