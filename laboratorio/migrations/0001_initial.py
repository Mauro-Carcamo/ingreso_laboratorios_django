# Generated by Django 4.2.5 on 2023-09-04 22:34

from django.db import migrations, models
import django.db.models.deletion
import laboratorio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('f_fabricacion', models.DateField(validators=[laboratorio.models.validate_min_date])),
                ('p_costo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('p_venta', models.DecimalField(decimal_places=2, max_digits=12)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laboratorio.laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('laboratorio', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='laboratorio.laboratorio')),
            ],
        ),
    ]
