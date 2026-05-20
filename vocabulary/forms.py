from django import forms
from django.core.validators import RegexValidator
from .models import Word, Language

word_validate = RegexValidator(
    regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s-]+$',
    message="This field cannot contain special characters or numbers. Only letters and spaces are allowed."
)

code_validate = RegexValidator(
    regex=r'^[a-z]{2,5}$',
    message="The language code must be 2 to 5 lowercase letters (e.g., 'es', 'en')."
)

class LanguageForm(forms.ModelForm):
    code = forms.CharField(max_length=5, validators=[code_validate], widget=forms.TextInput(attrs={'placeholder': 'e.g., en'}))
    name = forms.CharField(max_length=50, validators=[word_validate], widget=forms.TextInput(attrs={'placeholder': 'e.g., English'}))

    class Meta:
        model = Language
        fields = ['code', 'name']


class WordForm(forms.ModelForm):
    text = forms.CharField(max_length=100, validators=[word_validate], widget=forms.TextInput(attrs={'placeholder': 'Enter word...'}))

    class Meta:
        model = Word
        fields = ["text", "language", "translations"]
        widgets = {
            'translations': forms.CheckboxSelectMultiple(),
        }