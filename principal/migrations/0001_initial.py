# Generated by Django 4.1.7 on 2023-03-15 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.IntegerField()),
                ('color', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('direccion', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='principal.animal')),
                ('raza', models.CharField(max_length=256)),
                ('pelaje', models.CharField(max_length=256)),
            ],
            bases=('principal.animal',),
        ),
        migrations.CreateModel(
            name='Otro',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='principal.animal')),
                ('raza', models.CharField(max_length=256)),
                ('pelaje', models.CharField(max_length=256)),
            ],
            bases=('principal.animal',),
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='principal.animal')),
                ('raza', models.CharField(max_length=256)),
                ('pelaje', models.CharField(max_length=256)),
            ],
            bases=('principal.animal',),
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('departamento', models.CharField(max_length=256)),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.centro')),
            ],
        ),
        migrations.CreateModel(
            name='Adopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.animal')),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.centro')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.cliente')),
            ],
        ),
    ]