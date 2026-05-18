from django.db import models

class Word(models.Model):

    LANGUAGE_CHOICES = [
        ('sp', 'Spanish'),
        ('en', 'English'),
        ('pl', 'Polski'),
    ]

    original = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    

    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='es',
    )

    def __str__(self):
        return f"{self.original} -> {self.translation} ({self.get_language_display()})"