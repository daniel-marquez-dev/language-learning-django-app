from django.db import models

class Word(models.Model):
   original = models.CharField(max_length=100)
   translation = models.CharField(max_length=100)
   language = models.CharField(max_length=50)
 
   def __str__(self):
       return f"{self.original} - {self.translation}"
