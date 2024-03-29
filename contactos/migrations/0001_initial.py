# Generated by Django 2.2.6 on 2019-11-03 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=15)),
                ('compania', models.CharField(choices=[('Tigo', 'Tigo Guatemala'), ('Claro', 'Claro Guatemala'), ('Twenty', 'Twenty America'), ('Movistar', 'Movistar')], max_length=8)),
            ],
            options={
                'verbose_name': 'Telefono',
                'verbose_name_plural': 'Telefonos',
            },
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contactos.Telefono')),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
            },
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=50)),
                ('departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contactos.Departamento')),
            ],
            options={
                'verbose_name': 'Inscrito',
                'verbose_name_plural': 'Inscritos',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacto_num', models.CharField(max_length=15)),
                ('inscrito_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contactos.Inscrito')),
                ('responsable_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contactos.Responsable')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]
