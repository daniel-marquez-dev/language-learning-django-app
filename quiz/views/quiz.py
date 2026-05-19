from django.shortcuts import render, redirect
from django.db.models.functions import Length
from vocabulary.models import Word
import re

def quiz_view(request):
    if 'score' not in request.session:
        request.session['score'] = 0
       
    if 'seen_words' not in request.session:
        request.session['seen_words'] = []

    result = request.session.pop('quiz_result', None)
   
    language_choice = request.GET.get('language')
    difficulty = request.GET.get('difficulty', 'all')
    last_language = request.session.get('last_language')

    if language_choice != last_language:
        request.session['score'] = 0
        request.session['seen_words'] = []
        request.session['last_language'] = language_choice
        request.session.modified = True

    if request.method == "POST":
        word_id = request.POST.get("word_id")
       
        if word_id:
            word_id_int = int(word_id)
            if word_id_int not in request.session['seen_words']:
                request.session['seen_words'].append(word_id_int)
       
        raw_answer = request.POST.get("answer", "").lower().strip()
        
        # ⚠️ CORRECCIÓN AQUÍ: Cambiamos re.sub para que ELIMINE lo que NO son letras.
        # Añadimos el símbolo '^' al principio de los corchetes.
        user_answer = re.sub(r'[^a-záéíóúñü\s-]', '', raw_answer)
        
        word_obj = Word.objects.get(id=word_id)

        if user_answer == word_obj.translation.lower().strip():
            request.session['quiz_result'] = f"¡Correct! {word_obj.original} is {word_obj.translation}"
            request.session['score'] += 1
        else:
            request.session['quiz_result'] = f"Error {word_obj.original} was {word_obj.translation}"
            request.session['score'] -= 1
       
        request.session.modified = True
       
        return redirect(f"{request.path}?language={language_choice or ''}&difficulty={difficulty}")

    else:
        # 🆕 OBTENER IDIOMAS DINÁMICOS: Buscamos todos los idiomas únicos en la BD
        available_languages = Word.objects.values_list('language', flat=True).distinct().order_by('language')

        words = Word.objects.all()
       
        if language_choice:
            words = words.filter(language__iexact=language_choice)

        if difficulty == 'easy':
            words = words.annotate(text_len=Length('original')).filter(text_len__lte=4)
        elif difficulty == 'medium':
            words = words.annotate(text_len=Length('original')).filter(text_len__range=(5, 8))
        elif difficulty == 'hard':
            words = words.annotate(text_len=Length('original')).filter(text_len__gt=8)

        words = words.exclude(id__in=request.session['seen_words'])
        selected_word = words.order_by('?').first()

        if not selected_word and request.session['seen_words']:
            request.session['seen_words'] = []
            request.session.modified = True
            
            words = Word.objects.all()
            if language_choice:
                words = words.filter(language__iexact=language_choice)
            if difficulty == 'easy':
                words = words.annotate(text_len=Length('original')).filter(text_len__lte=4)
            elif difficulty == 'medium':
                words = words.annotate(text_len=Length('original')).filter(text_len__range=(5, 8))
            elif difficulty == 'hard':
                words = words.annotate(text_len=Length('original')).filter(text_len__gt=8)
            selected_word = words.order_by('?').first()

    return render(request, "quiz/quiz_page.html", {
        "word": selected_word,
        "result": result,
        "current_language": language_choice,
        "current_difficulty": difficulty,
        "score": request.session['score'],
        "available_languages": available_languages  # 🆕 Pasamos la lista al HTML
    })