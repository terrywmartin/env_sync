# Generated by Django 4.2.5 on 2023-09-28 16:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apikeys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9722a8dd-0bde-4477-b658-8e76e509efbb'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
