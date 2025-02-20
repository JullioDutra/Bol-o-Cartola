from django.urls import path
from . import views

urlpatterns = [
    path('', views.showcartolandia, name='make_prediction'),
    path('obrigado/', views.obrigado, name='thank_you'),
]
