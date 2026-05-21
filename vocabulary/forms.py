from django import forms  
from django.core.validators import RegexValidator  
from .models import Word, Language

# --- VALIDATORS ---

word_validate = RegexValidator(
    regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s-]+$',
    message="This field cannot contain special characters or numbers. Only letters and spaces are allowed."
)

code_validate = RegexValidator(
    regex=r'^[a-z]{2,5}$',
    message="The language code must be 2 to 5 lowercase letters (e.g., 'es', 'en')."
)

# --- FORMS ---

class LanguageForm(forms.ModelForm):
    code = forms.CharField(
        max_length=5, 
        validators=[code_validate], 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., en'}) # Added bootstrap 'form-control' class to keep the design clean
    )
    name = forms.CharField(
        max_length=50, 
        validators=[word_validate], 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., English'})
    )

    class Meta:
        model = Language
        fields = ['code', 'name']


class QuickWordTranslationForm(forms.Form):
    # Source Word Section
    word_text = forms.CharField(
        max_length=100, 
        validators=[word_validate], 
        label="Source Word",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Hello'})
    )
    word_language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        label="Word Language",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # Direct Translation Section
    translation_text = forms.CharField(
        max_length=100, 
        validators=[word_validate], 
        label="Translation",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Hola'})
    )
    translation_language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        label="Translation Language",
        widget=forms.Select(attrs={'class': 'form-select'})
    )