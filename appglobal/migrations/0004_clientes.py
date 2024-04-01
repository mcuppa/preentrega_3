# Generated by Django 5.0.3 on 2024-04-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appglobal', '0003_accesorios'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=200)),
                ('condition', models.CharField(choices=[('opción1', 'Opción 1'), ('opción2', 'Opción 2'), ('opción3', 'Opción 3')], max_length=20)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
