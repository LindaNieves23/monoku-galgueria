# Generated by Django 2.1 on 2018-12-07 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galguerias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=200)),
                ('tipo_producto', models.CharField(max_length=200)),
                ('fecha_vencimiento', models.CharField(max_length=200)),
                ('cantidad_producto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=200)),
                ('cargo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Preferecias_galguerias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_consumido', models.CharField(max_length=200)),
                ('nombre_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monoku.Personas')),
                ('nombre_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monoku.Galguerias')),
            ],
        ),
    ]
