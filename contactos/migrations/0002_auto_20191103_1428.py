# Generated by Django 2.2.6 on 2019-11-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='contacto_num',
            field=models.CharField(default='N/A', max_length=15, null=True),
        ),
    ]