# Generated by Django 5.0.1 on 2024-02-16 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=64, null=True, unique=True)),
                ('author', models.CharField(blank=True, max_length=128, null=True)),
                ('genre', models.CharField(blank=True, default='Жанр', max_length=64, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Not read', 'NR'), ('Read', 'R'), ('Pending', 'P')], default='Not read', max_length=16)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('booked_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
    ]
