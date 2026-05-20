from django.shortcuts import render, redirect
from .models import Word, Language
from .forms import WordForm, LanguageForm


def index(request):
    return render(request, 'vocabulary/index.html')



def word_list(request):

    words = Word.objects.all().order_by('language__name')
    return render(request, "vocabulary/dictionary.html", {"words": words})



def add_word(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dictionary") 
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