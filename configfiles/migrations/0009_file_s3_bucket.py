# Generated by Django 4.2.5 on 2023-10-01 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configfiles', '0008_alter_location_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='s3_bucket',
            field=models.TextField(blank=True, null=True),
        ),
    ]
