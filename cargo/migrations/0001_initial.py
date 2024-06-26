# Generated by Django 5.0.3 on 2024-03-28 16:04

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Weight')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='locations.location', to_field='zip', verbose_name='Location delivery')),
                ('pick_up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pick_up', to='locations.location', to_field='zip', verbose_name='Location pick-up')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargo',
            },
        ),
    ]
