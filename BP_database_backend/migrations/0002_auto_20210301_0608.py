# Generated by Django 3.1.7 on 2021-03-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP_database_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='file_datapack',
            field=models.FileField(blank=True, null=True, upload_to='datapack/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
