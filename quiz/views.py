import random
from django.shortcuts import render, redirect
from vocabulary.models import Word

def quiz_view(request):
    if 'score' not in request.session:
        request.session['score'] = 0

    result = request.session.pop('quiz_result', None)
    
    # Recuperamos parámetros de la URL
    language_choice = request.GET.get('language')
    difficulty = request.GET.get('difficulty', 'all') # Por defecto 'all'
    last_language = request.session.get('last_language')

    # Reset de puntuación si cambia el idioma
    if language_choice != last_language:
        request.session['score'] = 0
        request.session['last_language'] = language_choice
        request.session.modified = True

    if request.method == "POST":
        word_id = request.POST.get("word_id")
        user_answer = request.POST.get("answer", "").lower().strip()
        word_obj = Word.objects.get(id=word_id)

        if user_answer == word_obj.translation.lower().strip():
            request.session['quiz_result'] = f"✅ ¡Correcto! {word_obj.original} es {word_obj.translation}"
            request.session['score'] += 1
        else:
            request.session['quiz_result'] = f"❌ Error. {word_obj.original} era {word_obj.translation}"
            request.session['score'] -= 1
        
        request.session.modified = True
        
        # Al redirigir mantenemos idioma y dificultad
        return redirect(f"{request.path}?language={language_choice or ''}&difficulty={difficulty}")

    else:
        words = Word.objects.all()
        if language_choice:
            words = words.filter(language__iexact=language_choice)

        # --- LÓGICA DE DIFICULTAD ---
        if difficulty == 'easy':
            # Palabras de 1 a 4 letras
            words = [w for w in words if len(w.original) <= 4]
        elif difficulty == 'medium':
            # Palabras de 5 a 8 letras
            words = [w for w in words if 5 <= len(w.original) <= 8]
        elif difficulty == 'hard':
            # Palabras de más de 8 letras
            words = [w for w in words if len(w.original) > 8]

        if words: # Si la lista filtrada tiene palabras
            selected_word = random.choice(words)
        else:
            selected_word = None

    return render(request, "quiz/quiz_page.html", {
        "word": selected_word,
        "result": result,
        "current_language": language_choice,
        "current_difficulty": difficulty,
        "score": request.session['score']
    })