from django.db import models

class Employee(models.Model):
    tab_number = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name