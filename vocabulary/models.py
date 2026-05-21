from django.db import models

class Language(models.Model):
    
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.name:
            self.name = self.name.strip().capitalize()
        if self.code:
            self.code = self.code.strip().lower()


class Word(models.Model):
    text = models.CharField(max_length=100, verbose_name="Word")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="words", verbose_name="Language")

    translations = models.ManyToManyField('self', symmetrical=True, blank=True, verbose_name="Translations")

    def __str__(self):
        return f"{self.text} ({self.language.code.upper()})"