import random
from django.shortcuts import render
from vocabulary.models import Word

def quiz_view(request):
    result = None
    selected_word = None
    
    # 1. Inicializar el contador en la sesión si no existe
    if 'score' not in request.session:
        request.session['score'] = 0

    language_choice = request.GET.get('language') 

    if request.method == "POST":
        word_id = request.POST.get("word_id")
        user_answer = request.POST.get("answer").lower().strip()
        correct_word = Word.objects.get(id=word_id)
        
        language_choice = correct_word.language 

        if user_answer == correct_word.translation.lower().strip():
            result = f"✅ ¡Correcto! {correct_word.original} es {correct_word.translation}."
            # 2. Sumar punto
            request.session['score'] += 1
        else:
            result = f"❌ Error. {correct_word.original} se traduce como {correct_word.translation}."
            # 3. Restar punto
            request.session['score'] -= 1
        
        # Avisamos a Django que la sesión ha cambiado para que guarde el punto
        request.session.modified = True
        selected_word = correct_word 
    
    else:
        words = Word.objects.all()
        if language_choice:
            words = words.filter(language__iexact=language_choice)

        if words.exists():
            selected_word = random.choice(words)

    return render(request, "quiz/quiz_page.html", {
        "word": selected_word,
        "result": result,
        "current_language": language_choice,
        "score": request.session['score'] # 4. Enviamos el puntaje al HTML
    })