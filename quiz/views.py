import random
from django.shortcuts import render, redirect
from vocabulary.models import Word

def quiz_view(request):
    # 1. Asegurar que el score exista en la sesión
    if 'score' not in request.session:
        request.session['score'] = 0

    # 2. Recuperar el mensaje del intento anterior (si existe)
    result = request.session.pop('quiz_result', None)
    
    # 3. Obtener el idioma de la URL y el de la sesión para comparar
    language_choice = request.GET.get('language')
    last_language = request.session.get('last_language')

    # 4. RESET de puntuación: Solo si el idioma seleccionado es distinto al anterior
    if language_choice != last_language:
        request.session['score'] = 0
        request.session['last_language'] = language_choice
        request.session.modified = True

    if request.method == "POST":
        word_id = request.POST.get("word_id")
        user_answer = request.POST.get("answer", "").lower().strip()
        word_obj = Word.objects.get(id=word_id)

        # Lógica de puntuación
        if user_answer == word_obj.translation.lower().strip():
            request.session['quiz_result'] = f"✅ ¡Correcto! {word_obj.original} es {word_obj.translation}"
            request.session['score'] += 1
        else:
            request.session['quiz_result'] = f"❌ Error. {word_obj.original} era {word_obj.translation}"
            request.session['score'] -= 1
        
        request.session.modified = True
        
        # Redirigimos para cargar una nueva palabra al azar
        return redirect(f"{request.path}?language={language_choice or ''}")

    else:
        # 5. Selección puramente aleatoria
        words = Word.objects.all()
        if language_choice:
            words = words.filter(language__iexact=language_choice)

        if words.exists():
            # Elige cualquier palabra de la lista sin filtros de historial
            selected_word = random.choice(words)
        else:
            selected_word = None

    return render(request, "quiz/quiz_page.html", {
        "word": selected_word,
        "result": result,
        "current_language": language_choice,
        "score": request.session['score']
    })