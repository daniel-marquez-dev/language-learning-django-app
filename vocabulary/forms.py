import re
from django import forms
from .models import Language, Word
from django.core.validators import RegexValidator


word_validate = RegexValidator(
    regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s-]+$',
    message="This field cannot contain special characters like @, _, /, or numbers. Only letters and spaces are allowed."
)


code_validate = RegexValidator(
    regex=r'^[a-z]{2,5}$',
    message="The language code must be 2 to 5 lowercase letters (e.g., 'es', 'en')."
)



class WordForm(forms.ModelForm):
    original = forms.CharField(validators=[word_validate])
    translation = forms.CharField(validators=[word_validate])

    class Meta:
        model = Word
        fields = ["original", "translation", "language"]



class LanguageForm(forms.ModelForm):  

    code = forms.CharField(
        max_length=5,
        validators=[code_validate],
        widget=forms.TextInput(attrs={'placeholder': 'e.g., en, es, pl'})
    )
    name = forms.CharField(
        max_length=50,
        validators=[word_validate],
        widget=forms.TextInput(attrs={'placeholder': 'e.g., English, Spanish, Polski'})
    )

    class Meta:  
        model = Language
        fields = ['code', 'name']