# Generated by Django 3.1.7 on 2021-03-15 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BP_database_backend', '0002_auto_20210301_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(blank=True, choices=[('Blockchain', 'Blockchain'), ('Consumer_product&service', 'Consumer_product&service'), ('Content', 'Content'), ('Enterprise_service', 'Enterprise_service'), ('E-commerce', 'E-commerce'), ('Industrial_internet', 'Industrial_internet'), ('FinTech', 'Fintech'), ('Core_tech', 'Core_tech'), ('Social_media', 'Social_media'), ('Education', 'Education'), ('Healthcare', 'Healthcare'), ('Travel_accommodation_tourism', 'Travel_accommodation_tourism'), ('Unclassified', 'Unclassified')], max_length=50, null=True),
        ),
    ]
