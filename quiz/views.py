import random
from django.shortcuts import render, redirect
from vocabulary.models import Word, Language

def quiz_view(request):
    if 'score' not in request.session:
        request.session['score'] = 0

    result = request.session.pop('quiz_result', None)
    
    # NUEVO: Capturamos idioma de origen e idioma de destino
    from_lang = request.GET.get('from_lang') # Ej: "Spanish", "English"
    to_lang = request.GET.get('to_lang')     # Ej: "English", "Polski"
    
    difficulty = request.GET.get('difficulty', 'all') 
    
    # Control de reinicio de puntuación si cambia la combinación de idiomas
    last_combo = request.session.get('last_combo', '')
    current_combo = f"{from_lang}-{to_lang}"
    if current_combo != last_combo:
        request.session['score'] = 0
        request.session['last_combo'] = current_combo
        request.session.modified = True

    # --- PROCESAR LA RESPUESTA DEL USUARIO ---
    if request.method == "POST":
        word_id = request.POST.get("word_id") # ID de la palabra reto (en el idioma 'from_lang')
        user_answer = request.POST.get("answer", "").lower().strip()
        word_obj = Word.objects.get(id=word_id)

        # FILTRADO MULTIDIRECCIONAL: Buscamos traducciones de la palabra reto
        # pero estrictamente las que pertenezcan al idioma destino ('to_lang')
        valid_answers = [
            t.text.lower().strip() 
            for t in word_obj.translations.filter(language__name__iexact=to_lang)
        ]

        if user_answer in valid_answers:
            request.session['quiz_result'] = f"✅ ¡Correcto! La traducción de '{word_obj.text}' es '{user_answer.capitalize()}'."
            request.session['score'] += 1
        else:
            correct_expected = word_obj.translations.filter(language__name__iexact=to_lang).first()
            correct_text = correct_expected.text if correct_expected else "unknown"
            request.session['quiz_result'] = f"❌ Incorrecto. '{word_obj.text}' en {to_lang} se dice '{correct_text}'."
            request.session['score'] -= 1
        
        request.session.modified = True
        return redirect(f"{request.path}?from_lang={from_lang or ''}&to_lang={to_lang or ''}&difficulty={difficulty}")

    # --- MOSTRAR UNA NUEVA PALABRA AL AZAR ---
    else:
        selected_word = None
        # Solo buscamos si el usuario ha seleccionado ambos extremos del juego
        if from_lang and to_lang:
            # Buscamos palabras que pertenezcan al idioma origen Y que tengan traducción al idioma destino
            words_pool = Word.objects.filter(
                language__name__iexact=from_lang, 
                translations__language__name__iexact=to_lang
            ).distinct()

            # Filtrado por dificultad basado en la longitud de la traducción que el usuario debe escribir
            filtered_words = []
            for w in words_pool:
                target_trans = w.translations.filter(language__name__iexact=to_lang).first()
                if target_trans:
                    word_len = len(target_trans.text)
                    if difficulty == 'easy' and word_len <= 4:
                        filtered_words.append(w)
                    elif difficulty == 'medium' and 5 <= word_len <= 8:
                        filtered_words.append(w)
                    elif difficulty == 'hard' and word_len > 8:
                        filtered_words.append(w)
                    elif difficulty == 'all':
                        filtered_words.append(w)

            if filtered_words:
                selected_word = random.choice(filtered_words)

        # Pasamos a la plantilla todos los idiomas disponibles para llenar los selectores dinámicamente
        languages = Language.objects.all()

    return render(request, "quiz/quiz_page.html", {
        "word": selected_word,
        "result": result,
        "from_lang": from_lang,
        "to_lang": to_lang,
        "languages": languages,
        "current_difficulty": difficulty,
        "score": request.session['score']
    })