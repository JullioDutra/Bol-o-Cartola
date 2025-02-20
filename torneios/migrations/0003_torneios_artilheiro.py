# Generated by Django 5.1.6 on 2025-02-19 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artilheiros', '0001_initial'),
        ('torneios', '0002_torneios_campeao_torneios_finalistas'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneios',
            name='artilheiro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top_scorer_in', to='artilheiros.artilheiro'),
        ),
    ]
