# Generated by Django 5.1.5 on 2025-02-04 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(blank=True, max_length=200, verbose_name='имя покемона на русском')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='имя покемона на английском')),
                ('title_jp', models.CharField(blank=True, max_length=200, verbose_name='имя покемона на японском')),
                ('images', models.ImageField(blank=True, null=True, upload_to='pocemons_images/', verbose_name='изображение покемона')),
                ('description', models.TextField(verbose_name='описание')),
                ('previous_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='предыдущая эволюция покемона')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appear_at', models.DateTimeField(verbose_name='дата и время появления')),
                ('disappear_at', models.DateTimeField(blank=True, null=True, verbose_name='дата и время исчезновения')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='Уровень')),
                ('health', models.PositiveIntegerField(default=1, verbose_name='Здоровье')),
                ('strength', models.PositiveIntegerField(default=1, verbose_name='Атака')),
                ('defence', models.PositiveIntegerField(default=1, verbose_name='Защита')),
                ('stamina', models.PositiveIntegerField(default=1, verbose_name='Выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon', verbose_name='покемон')),
            ],
        ),
    ]
