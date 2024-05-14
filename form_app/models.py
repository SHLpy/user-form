from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.email})"

