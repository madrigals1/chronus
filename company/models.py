from django.db import models


class Company(models.Model):
    TYPES = [
        ('private', 'Private Company'),
        ('company', 'Public Company')
    ]

    name = models.CharField(max_length=100, blank=False, default='')
    type = models.CharField(max_length=32, choices=TYPES, default='private')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    company = models.ForeignKey(
        'company.Company', on_delete=models.CASCADE, related_name='teams'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def company_name(self):
        return self.company.name

    def __str__(self):
        return f'{self.company_name} - {self.name}'
