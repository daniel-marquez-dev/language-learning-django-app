from django.shortcuts import render
from .models import Word


# DISPLAYING WORDS VIEW (DIA 3)
def word_list(request):
    words = Word.objects.all()
    return render(request, "vocabulary/word_list.html", {"words": words})

from django.shortcuts import render, redirect
from .forms import WordForm

# VIEW FOR ADDING WORDS (DIA 4)
def add_word(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("word_list")  # Te devuelve a la lista de palabras
    else:
        form = WordForm()
    return render(request, "vocabulary/add_word.html", {"form": form})
