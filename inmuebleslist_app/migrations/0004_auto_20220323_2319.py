# Generated by Django 3.2.8 on 2022-03-24 04:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0003_edificacion_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificacion',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edificacionlist', to='inmuebleslist_app.empresa'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('texto', models.CharField(max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('edificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='inmuebleslist_app.edificacion')),
            ],
        ),
    ]
