# Generated by Django 5.0.6 on 2024-07-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_cliente_clientes_alter_clientes_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='foto_cliente',
            field=models.ImageField(default='static/img/imagenes_clientes/default.jpg', upload_to='static/img/imagenes_clientes/', verbose_name='Foto del Cliente'),
        ),
    ]
