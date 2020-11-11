# Generated by Django 3.1.2 on 2020-11-11 07:10

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_usuario_temas_preferidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Cedula',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Ciudad',
            field=models.IntegerField(blank=True, choices=[('Armenia', 'Armenia'), ('Barranquilla', 'Barranquilla'), ('Bello', 'Bello'), ('Bogotá', 'Bogotá'), ('Bucaramanga', 'Bucaramanga'), ('Cali', 'Cali'), ('Cartagena', 'Cartagena'), ('Cúcuta', 'Cúcuta'), ('Ibagué', 'Ibagué'), ('Manizales', 'Manizales'), ('Medellín', 'Medellín'), ('Montería', 'Montería'), ('Neiva', 'Neiva'), ('Cartagena', 'Cartagena'), ('Pasto', 'Pasto'), ('Pereira', 'Pereira'), ('Santa Marta', 'Santa Marta'), ('Soacha', 'Soacha'), ('Soledad', 'Soledad'), ('Valledupar', 'Valledupar'), ('Villavicencio', 'Villavicencio')], default='Pereira', max_length=200, null=True, verbose_name='Ciudad de residencia'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.IntegerField(blank=True, choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('Otro', 'Otro')], default='Femenino', max_length=200, null=True, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='suscripcion',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Suscribirme a noticias'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='temas_preferidos',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Historia y Geografía', 'Historia y Geografía'), ('Narrativa', 'Narrativa'), ('Juvenil', 'Juvenil'), ('Ciencias físicas', 'Ciencias físicas'), ('Infantil', 'Infantil'), ('Ciencias Sociales y política', 'Ciencias Sociales y política'), ('Medicina y salud', 'Medicina y salud'), ('Filosofía', 'Filosofía'), ('Arquitectura', 'Arquitectura'), ('Arte', 'Arte'), ('Gastronomía', 'Gastronomía'), ('Varios', 'Varios')], default='Varios', max_length=157, null=True, verbose_name='Temas de preferencia'),
        ),
    ]