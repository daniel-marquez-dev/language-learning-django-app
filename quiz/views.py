import random
from django.shortcuts import render
from vocabulary.models import Word  # Importas el modelo desde la otra app

def quiz_view(request):
    result = None
    selected_word = None
    
    if request.method == "POST":
        word_id = request.POST.get("word_id")
        user_answer = request.POST.get("answer").lower().strip()
        correct_word = Word.objects.get(id=word_id)
        
        if user_answer == correct_word.translation.lower().strip():
            result = "✅ ¡Correcto!"
        else:
            result = f"❌ Incorrecto. Era: {correct_word.translation}"
        selected_word = correct_word 
    else:
        words = Word.objects.all()
        if words.exists():
            selected_word = random.choice(words)

    return render(request, "quiz/quiz_page.html", {
        "word": selected_word,
        "result": result
    })