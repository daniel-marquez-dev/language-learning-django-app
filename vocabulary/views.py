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

                # 🛡️ ESCUDO 1: Validar idioma de la palabra ORIGEN
                existing_word_different_lang = Word.objects.filter(text__iexact=w_text).exclude(language=w_lang).first()

                if existing_word_different_lang:
                    form.add_error(
                        'word_language', 
                        f'The word "{w_text}" is already registered under the language "{existing_word_different_lang.language.name}". You cannot assign it to "{w_lang.name}".'
                    )
                    return render(request, "vocabulary/add_word.html", {"form": form, "lang_form": lang_form})

                # 🛡️ ESCUDO 2: Validar idioma de la palabra TRADUCCIÓN
                existing_trans_different_lang = Word.objects.filter(text__iexact=t_text).exclude(language=t_lang).first()

                if existing_trans_different_lang:
                    form.add_error(
                        'translation_language', 
                        f'The translation "{t_text}" is already registered under the language "{existing_trans_different_lang.language.name}". You cannot assign it to "{t_lang.name}".'
                    )
                    return render(request, "vocabulary/add_word.html", {"form": form, "lang_form": lang_form})

                # 🔍 VALIDACIÓN 3: Verificar duplicados exactos ya vinculados
                word_exists = Word.objects.filter(text=w_text, language=w_lang).exists()
                trans_exists = Word.objects.filter(text=t_text, language=t_lang).exists()

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

                if word_exists and trans_exists:
                    form.add_error(None, "Both the source word and the translation already exist in the database as separate terms.")
                    return render(request, "vocabulary/add_word.html", {"form": form, "lang_form": lang_form})

                # Si el registro pasa todos los filtros de consistencia, se guarda
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