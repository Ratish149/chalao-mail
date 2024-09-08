from django.db import models

# Create your models here.

class Mail(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return f'{self.full_name} - {self.email}'