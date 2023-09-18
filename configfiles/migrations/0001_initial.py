# Generated by Django 4.2.5 on 2023-09-18 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigFile',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('535aa388-313a-4675-aefb-259a341d357b'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('c698c395-6808-4568-8b7e-d4cdbb5c8d85'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('99682d51-4e6f-4bfc-bcae-40fb61023d9e'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=250)),
                ('environment', models.CharField(blank=True, max_length=20, null=True)),
                ('config', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configfiles.configfile')),
            ],
        ),
    ]
