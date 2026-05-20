from django.db import models

class Language(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name="Language Code (e.g., 'en', 'es')")
    name = models.CharField(max_length=50, verbose_name="Language Name")

    def __str__(self):
        # Muestra por ejemplo: "Spanish (ES)"
        return f"{self.name} ({self.code.upper()})"


class Word(models.Model):
    original = models.CharField(max_length=100, verbose_name="Original Word")
    translation = models.CharField(max_length=100, verbose_name="Translation")
    
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="words", verbose_name="Language")

    def __str__(self):

        return f"{self.original} -> {self.translation} ({self.language.name})"