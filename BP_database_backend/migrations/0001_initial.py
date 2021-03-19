# Generated by Django 3.1.5 on 2021-02-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, choices=[('Blockchain', 'Blockchain'), ('Consumer_product&service', 'Consumer_product&service'), ('Content', 'Content'), ('Enterprise_service', 'Enterprise_service'), ('E_commerce', 'E_commerce'), ('Industrial_internet', 'Industrial_internet'), ('FinTech', 'Fintech'), ('Core_tech', 'Core_tech'), ('Social_media', 'Social_media'), ('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Travel_accommodation_tourism', 'Travel_accommodation_tourism'), ('Unclassified', 'Unclassified')], max_length=50, null=True)),
                ('submitter', models.CharField(max_length=30)),
                ('FA', models.CharField(max_length=30)),
                ('summary', models.TextField(blank=True, null=True)),
                ('file_BP', models.FileField(null=True, upload_to='BP/')),
                ('file_datapack', models.FileField(null=True, upload_to='datapack/')),
                ('last_update_time', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('passwd', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]