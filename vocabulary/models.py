from django.db import models

class Language(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name="Language Code (e.g., 'en', 'es')")
    name = models.CharField(max_length=50, verbose_name="Language Name")

    def __str__(self):
        return f"{self.name} ({self.code.upper()})"


class Word(models.Model):
    text = models.CharField(max_length=100, verbose_name="Word")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="words", verbose_name="Language")
    
    # Relación simétrica auto-referenciada
    translations = models.ManyToManyField('self', blank=True, verbose_name="Translations")

    def __str__(self):
        return f"{self.text} ({self.language.code.upper()})"