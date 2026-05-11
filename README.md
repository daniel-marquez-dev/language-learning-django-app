Quiz Module (Implemented by Intern 2)



Este módulo complementa el diccionario de vocabulario mediante una interfaz de aprendizaje interactiva, permitiendo a los usuarios poner a prueba sus conocimientos de manera dinámica.

Features Dynamic Language Filtering: Implementación de filtrado por idioma a través de parámetros en la URL, permitiendo sesiones de práctica personalizadas.

Session-Based Scoring: Sistema de puntuación persistente (+1 acierto, -1 fallo) utilizando django.contrib.sessions, lo que permite seguir el progreso sin necesidad de autenticación.

Randomized Learning Logic: Algoritmo que selecciona palabras de forma aleatoria de la base de datos para garantizar que cada sesión de estudio sea única.

Post/Redirect/Get Pattern: Implementación de redirecciones tras el envío de formularios para evitar el reenvío de datos al recargar y asegurar la integridad del puntaje.

State Management: Lógica inteligente de reinicio de puntuación que detecta cambios de idioma para mantener la coherencia en las métricas de aprendizaje.

UX-Focused Feedback: Sistema de mensajes temporales (Success/Error) integrados en el flujo de la sesión para retroalimentación inmediata del usuario.

Tech Stack Framework: Django 5.x

Language: Python 3.x

Session Management: Django Session Engine

Frontend: Django Templates (HTML/CSS)

Setup & Installation El proceso de instalación es el mismo que en el módulo principal.

Activar Entorno Virtual: (Ver instrucciones de Intern 1)

Migrar la Base de Datos:

Bash python manage.py migrate Poblar Vocabulario: Es necesario añadir palabras desde el panel de administración o el formulario de vocabulario antes de iniciar el Quiz.

Project Structure (Quiz App) views.py: Manejo de la lógica de puntuación, control de sesiones y selección aleatoria de términos.

urls.py: Mapeo de rutas para la vista principal del Quiz.

templates/quiz/: Interfaz de usuario dinámica que muestra la palabra a traducir, el resultado del intento anterior y el marcador actual.

Usage Iniciar Práctica General: http://127.0.0.1:8000/quiz/

Práctica por Idioma Específico: http://127.0.0.1:8000/quiz/?language=ingles

Siguiente Palabra: Utiliza el botón "Siguiente" para cambiar de término manteniendo tu puntuación actual.
