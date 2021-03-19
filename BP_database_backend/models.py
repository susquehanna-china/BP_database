from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)
    category_choices = (("Blockchain", 'Blockchain'),
                        ('Consumer_product&service', 'Consumer_product&service'),
                        ('Content', 'Content'),
                        ('Enterprise_service', 'Enterprise_service'),
                        ('E-commerce', 'E-commerce'),
                        ('Industrial_internet', 'Industrial_internet'),
                        ('FinTech', 'Fintech'),
                        ('Core_tech', 'Core_tech'),
                        ('Social_media', 'Social_media'),
                        ('Education', 'Education'),
                        ('Healthcare', 'Healthcare'),
                        ('Travel_accommodation_tourism', 'Travel_accommodation_tourism'),
                        ('Unclassified', 'Unclassified'))
    category = models.CharField(max_length=50, null=True, blank=True, choices=category_choices)
    submitter = models.CharField(max_length=30)
    FA = models.CharField(max_length=30)
    summary = models.TextField(null=True, )
    file_BP = models.FileField(upload_to='BP/', null=True)
    file_datapack = models.FileField(upload_to='datapack/', null=True, blank=True)
    last_update_time = models.DateField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=30)
    passwd = models.CharField(max_length=20)
    position = models.CharField(max_length=20, null=True, choices=(('Full-time', 'Full-time'), ('Intern', 'Intern')))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

