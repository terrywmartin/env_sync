# Generated by Django 4.2.5 on 2023-09-30 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configfiles', '0006_alter_configfile_id_alter_file_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
    ]
