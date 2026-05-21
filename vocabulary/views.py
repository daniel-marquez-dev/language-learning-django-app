import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Word, Language
from .forms import QuickWordTranslationForm, LanguageForm

def index(request):
    return render(request, 'vocabulary/index.html')


def word_list(request):
    words = Word.objects.all().order_by('text')
    search_query = request.GET.get('search')
    
    if search_query:
        words = words.filter(
            Q(text__icontains=search_query) | 
            Q(translations__text__icontains=search_query)
        ).distinct()
        
    return render(request, "vocabulary/word_list.html", {"words": words})


def add_word(request):
    form = QuickWordTranslationForm()
    lang_form = LanguageForm()

    if request.method == "POST":
        if "submit_word" in request.POST or "submit_and_continue" in request.POST:
            form = QuickWordTranslationForm(request.POST) 
            
            if form.is_valid():
                w_text = form.cleaned_data.get('word_text')
                w_lang = form.cleaned_data.get('word_language')
                t_text = form.cleaned_data.get('translation_text')
                t_lang = form.cleaned_data.get('translation_language')

                # 🚀 VALIDACIÓN DE DUPLICADOS:
                # Comprobamos si ya existe la palabra origen con su idioma
                word_exists = Word.objects.filter(text=w_text, language=w_lang).exists()
                # Comprobamos si ya existe la palabra traducción con su idioma
                trans_exists = Word.objects.filter(text=t_text, language=t_lang).exists()

                # Si ambas existen, comprobamos si además ya están conectadas entre sí
                if word_exists and trans_exists:
                    already_linked = Word.objects.filter(
                        text=w_text, 
                        language=w_lang, 
                        translations__text=t_text, 
                        translations__language=t_lang
                    ).exists()
                    
                    if already_linked:
                        form.add_error(None, f'The word "{w_text}" and its translation "{t_text}" are already registered and linked.')
                        return render(request, "vocabulary/add_word.html", {"form": form, "lang_form": lang_form})

                # Si no están vinculadas, pero quieres avisar de que los términos individuales ya existen por separado
                if word_exists and trans_exists:
                    form.add_error(None, "Both the source word and the translation already exist in the database as separate terms.")
                    return render(request, "vocabulary/add_word.html", {"form": form, "lang_form": lang_form})
                elif word_exists:
                    form.add_error(None, f'The source word "{w_text}" ({w_lang.name}) already exists in your dictionary.')
                    return render(request, "vocabulary/add_word.html", {"form": form, "lang_form": lang_form})
                elif trans_exists:
                    form.add_error(None, f'The translation word "{t_text}" ({t_lang.name}) already exists in your dictionary.')
                    return render(request, "vocabulary/add_word.html", {"form": form, "lang_form": lang_form})

                # Si pasa todas las validaciones, procedemos a guardar de forma segura
                word_obj, created = Word.objects.get_or_create(text=w_text, language=w_lang)
                translation_obj, _ = Word.objects.get_or_create(text=t_text, language=t_lang)
                word_obj.translations.add(translation_obj)

                messages.success(
                    request, 
                    f'The word "{w_text}" has been translated into {t_lang.name}: "{t_text}"'
                )
                
                if "submit_and_continue" in request.POST:
                    form = QuickWordTranslationForm(initial={
                        'word_text': w_text,
                        'word_language': w_lang
                    })
                    return render(request, "vocabulary/add_word.html", {
                        "form": form,
                        "lang_form": lang_form,
                    })
                    
                return redirect('index')

        elif "submit_language" in request.POST:
            lang_form = LanguageForm(request.POST) 
            
            if lang_form.is_valid():
                lang_form.save()
                messages.success(request, "Language added successfully!")
                return redirect('add_word')

    return render(request, "vocabulary/add_word.html", {
        "form": form,
        "lang_form": lang_form,
    })