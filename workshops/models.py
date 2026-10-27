from django.db import models

# Un modelo es una representación de una tabla

# tabla taller (workshop)
class Workshop(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    capacity = models.IntegerField()
    classroom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name