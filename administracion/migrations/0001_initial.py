# Generated by Django 3.2.8 on 2023-05-09 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNumber', models.IntegerField()),
                ('dispo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=15, null=True)),
                ('category', models.CharField(default='cliente', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField()),
                ('out_date', models.DateField()),
                ('ejecutada', models.BooleanField(default=False)),
                ('cancelada', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.userprofile')),
                ('habitaciones', models.ManyToManyField(related_name='reservaciones', to='administracion.Habitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=500)),
                ('doneResponse', models.BooleanField(default=False)),
                ('response', models.CharField(default='', max_length=500)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.habitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Hospedaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.habitacion')),
                ('reservacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospedajes', to='administracion.reservacion')),
            ],
        ),
    ]
