# Generated by Django 5.1.5 on 2025-02-02 16:27

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
                ('title', models.CharField(max_length=200)),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
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
                ('level', models.IntegerField(default=1, verbose_name='Уровень')),
                ('health', models.IntegerField(default=1, verbose_name='Здоровье')),
                ('strength', models.IntegerField(default=1, verbose_name='Атака')),
                ('defence', models.IntegerField(default=1, verbose_name='Защита')),
                ('stamina', models.IntegerField(default=1, verbose_name='Выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon', verbose_name='покемон')),
            ],
        ),
    ]
