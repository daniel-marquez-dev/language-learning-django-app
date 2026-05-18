from django import forms
from .models import Word
from django.core.validators import RegexValidator

class WordForm(forms.ModelForm):
    # 1. Definimos el validador
    word_validate = RegexValidator(
        regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s-]+$',
        message="The word cannot contain special characters like @, _, /, or numbers. Only letters and spaces are allowed."
    )

    original = forms.CharField(validators=[word_validate])
    translation = forms.CharField(validators=[word_validate])

    class Meta:
        model = Word
        fields = ["original", "translation", "language"]