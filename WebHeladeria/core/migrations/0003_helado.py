# Generated by Django 5.0.6 on 2024-07-14 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_clientes_foto_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Helado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]