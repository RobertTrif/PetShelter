# Generated by Django 4.2.1 on 2023-06-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_horario_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='centro',
            name='correo',
            field=models.CharField(default='correo@correo.correo', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centro',
            name='cp',
            field=models.IntegerField(default=5465456),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centro',
            name='telefono',
            field=models.IntegerField(default=56465465),
            preserve_default=False,
        ),
    ]
