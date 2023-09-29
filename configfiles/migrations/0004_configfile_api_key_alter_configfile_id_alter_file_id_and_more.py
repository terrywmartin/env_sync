# Generated by Django 4.2.5 on 2023-09-28 16:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apikeys', '0003_alter_apikey_id'),
        ('configfiles', '0003_file_location_alter_configfile_id_alter_file_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configfile',
            name='api_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apikeys.apikey'),
        ),
        migrations.AlterField(
            model_name='configfile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('21e26c2a-f67c-4725-aece-49ae92301323'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.UUIDField(default=uuid.UUID('54d0420d-8503-426e-9781-3300b4ef9ae0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c3f8edc0-6d65-42b5-a1bf-2b5df414be13'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]