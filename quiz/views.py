import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models.functions import Length, Trim
from vocabulary.models import Word, Language

def quiz_view(request):
    # Aseguramos que existan las variables de puntuación e historial
    if 'score' not in request.session:
        request.session['score'] = 0
    if 'answered_words' not in request.session:
        request.session['answered_words'] = []

    # Captura de parámetros estrictamente por GET
    ui_lang = request.GET.get('ui_lang', 'en')
    from_lang = request.GET.get('from_lang') or None
    to_lang = request.GET.get('to_lang') or None
    difficulty = request.GET.get('difficulty', 'all')
    
    selected_word = None
    
    if from_lang and to_lang:
        # Si el usuario cambia la combinación de idiomas, reiniciamos el juego
        last_combo = request.session.get('last_combo', '')
        current_combo = f"{from_lang}-{to_lang}"
        if current_combo != last_combo:
            request.session['score'] = 0
            request.session['last_combo'] = current_combo
            request.session['answered_words'] = []
            request.session.pop('current_word_id', None)

        # Intentamos recuperar la palabra que ya estaba guardada en esta sesión
        saved_word_id = request.session.get('current_word_id')
        if saved_word_id:
            try:
                selected_word = Word.objects.get(id=saved_word_id)
            except Word.DoesNotExist:
                pass
        
        # SI NO HAY PALABRA ACTIVA (porque venimos de quiz_next o es la primera vez)
        if not selected_word:
            # Buscamos todas las palabras que coincidan con los idiomas elegidos
            words_pool = Word.objects.filter(
                language__name__iexact=from_lang,
                translations__language__name__iexact=to_lang
            ).distinct()
            
            # Excluimos las palabras que ya se han respondido correctamente en esta sesión
            already_answered = request.session.get('answered_words', [])
            filtered_pool = words_pool.exclude(id__in=already_answered)
            
            # Limpiamos espacios en blanco y medimos longitud en BD para la dificultad
            filtered_pool = filtered_pool.annotate(texto_limpio=Trim('text')).annotate(texto_largo=Length('texto_limpio'))
            
            if difficulty == 'easy':
                filtered_pool = filtered_pool.filter(texto_largo__lte=4)
            elif difficulty == 'medium':
                filtered_pool = filtered_pool.filter(texto_largo__gte=5, texto_largo__lte=8)
            elif difficulty == 'hard':
                filtered_pool = filtered_pool.filter(texto_largo__gt=8)
            
            filtered_words = list(filtered_pool)
            
            if filtered_words:
                # Si hay palabras disponibles que no se han respondido, elegimos una al azar
                selected_word = random.choice(filtered_words)
                request.session['current_word_id'] = selected_word.id
            else:
                # ¡AQUÍ ESTÁ EL ARREGLO!: Si no quedan palabras nuevas en ese nivel/idioma, 
                # vaciamos el historial de respondidas para que pueda volver a usarlas todas.
                request.session['answered_words'] = []
                request.session.modified = True
                
                # Volvemos a evaluar el total de palabras del pool original con la dificultad
                words_pool = words_pool.annotate(texto_limpio=Trim('text')).annotate(texto_largo=Length('texto_limpio'))
                if difficulty == 'easy':
                    words_pool = words_pool.filter(texto_largo__lte=4)
                elif difficulty == 'medium':
                    words_pool = words_pool.filter(texto_largo__gte=5, texto_largo__lte=8)
                elif difficulty == 'hard':
                    words_pool = words_pool.filter(texto_largo__gt=8)
                
                backup_words = list(words_pool)
                if backup_words:
                    selected_word = random.choice(backup_words)
                    request.session['current_word_id'] = selected_word.id

    languages = Language.objects.all()
    
    return render(request, "quiz/quiz_page.html", {
        "word": selected_word,
        "from_lang": from_lang,
        "to_lang": to_lang,
        "languages": languages,
        "current_difficulty": difficulty,
        "score": request.session['score']
    })


def quiz_check(request):
    """ Vista dedicada exclusivamente a evaluar el formulario por POST """
    if request.method != "POST":
        return redirect('/quiz/')
        
    word_id = request.POST.get("word_id")
    user_answer = request.POST.get("answer", "").lower().strip()
    ui_lang = request.POST.get("ui_lang", "en")
    from_lang = request.POST.get("from_lang", "")
    to_lang = request.POST.get("to_lang", "")
    difficulty = request.POST.get("difficulty", "all")
    
    try:
        word_obj = Word.objects.get(id=word_id)
        translations = word_obj.translations.filter(language__name__iexact=to_lang)
        valid_answers = [t.text.lower().strip() for t in translations]
        
        if user_answer in valid_answers:
            if ui_lang == 'es':
                msg = f"✅ ¡Correcto! La traducción de '{word_obj.text}' es '{user_answer.capitalize()}'."
            elif ui_lang == 'pl':
                msg = f"✅ Dobrze! Tłumaczenie '{word_obj.text}' to '{user_answer.capitalize()}'."
            else:
                msg = f"✅ Correct! The translation of '{word_obj.text}' is '{user_answer.capitalize()}'."
            messages.success(request, msg)
            
            # Guardamos en el historial para que no vuelva a salir en el próximo ciclo
            if word_obj.id not in request.session.get('answered_words', []):
                request.session.setdefault('answered_words', []).append(word_obj.id)
            request.session['score'] = request.session.get('score', 0) + 1
        else:
            correct_text = translations.first().text if translations.exists() else "unknown"
            if ui_lang == 'es':
                msg = f"❌ Incorrecto. '{word_obj.text}' en {to_lang} se dice '{correct_text}'."
            elif ui_lang == 'pl':
                msg = f"❌ Niepoprawnie. '{word_obj.text}' po {to_lang} to '{correct_text}'."
            else:
                msg = f"❌ Incorrect. '{word_obj.text}' in {to_lang} is '{correct_text}'."
            messages.error(request, msg)
            
            request.session['score'] = max(0, request.session.get('score', 0) - 1)
            
    except Word.DoesNotExist:
        messages.error(request, "Error: Word not found.")

    # Almacenamos que el usuario ya respondió esta palabra para que aparezca el botón Siguiente
    request.session['has_answered'] = True
    request.session.modified = True
    
    return redirect(f"/quiz/?ui_lang={ui_lang}&from_lang={from_lang}&to_lang={to_lang}&difficulty={difficulty}")


def quiz_next(request):
    """ Vista dedicada exclusivamente a limpiar la palabra actual y saltar """
    ui_lang = request.GET.get('ui_lang', 'en')
    from_lang = request.GET.get('from_lang', '')
    to_lang = request.GET.get('to_lang', '')
    difficulty = request.GET.get('difficulty', 'all')
    
    # Borrado absoluto para forzar al GET a generar una palabra distinta
    request.session.pop('current_word_id', None)
    request.session.pop('has_answered', None)
    request.session.modified = True
    
    return redirect(f"/quiz/?ui_lang={ui_lang}&from_lang={from_lang}&to_lang={to_lang}&difficulty={difficulty}")