import random
from django.shortcuts import render, redirect
from django.db.models import Q
from vocabulary.models import Word, Language
from vocabulary.forms import WordForm, LanguageForm

# --- VISTAS DE VOCABULARY ---

def index(request):
    return render(request, 'vocabulary/index.html')


def word_list(request):
    words = Word.objects.all().order_by('text')
    search_query = request.GET.get('search')
    
    if search_query:
        # Busca por el texto de la palabra O por el texto de cualquiera de sus traducciones
        words = words.filter(
            Q(text__icontains=search_query) | 
            Q(translations__text__icontains=search_query)
        ).distinct()
        
    return render(request, "vocabulary/word_list.html", {"words": words})


def add_word(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("word_list")
    else:
        form = WordForm()
    return render(request, "vocabulary/add_word.html", {"form": form})


def add_language(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = LanguageForm()
    return render(request, "vocabulary/add_language.html", {"form": form})