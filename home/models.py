from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    year = models.PositiveBigIntegerField()
    created = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.owner} - {self.name} - {self.year}"