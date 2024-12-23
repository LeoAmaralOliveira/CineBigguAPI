# Generated by Django 4.2.16 on 2024-12-05 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemabiggu', '0007_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemabiggu.movie')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemabiggu.room')),
            ],
        ),
        migrations.CreateModel(
            name='SessionPriceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('half_price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('fan_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemabiggu.session')),
            ],
        ),
    ]
