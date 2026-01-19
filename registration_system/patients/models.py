from django.db import models
from .validators import validate_cpf

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    CPF = models.CharField(
        max_length=14, 
        unique=True,
        validators=[validate_cpf]
    )
    birth_date = models.DateField()
    
    gender = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ]
    )
    
    address = models.CharField(max_length=150)
    admission_date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name