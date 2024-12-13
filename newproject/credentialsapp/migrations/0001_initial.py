# Generated by Django 5.1.4 on 2024-12-13 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('practice_name', models.CharField(max_length=255, null=True)),
                ('notes', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('system_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('notes', models.TextField(null=True)),
                ('practitioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credentialsapp.practitioner')),
            ],
        ),
    ]
