# Generated by Django 5.0.3 on 2024-04-01 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appglobal', '0004_clientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='condition',
            field=models.CharField(choices=[('consumidor_final', 'Consumidor final'), ('monotributista', 'Monotributista'), ('responsable_inscripto', 'Responsable inscripto'), ('exento', 'Exento')], max_length=30),
        ),
    ]