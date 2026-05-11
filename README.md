<<<<<<< HEAD
Quiz Module (Implemented by Intern 2)


<<<<<<< HEAD

Este módulo complementa el diccionario de vocabulario mediante una interfaz de aprendizaje interactiva, permitiendo a los usuarios poner a prueba sus conocimientos de manera dinámica.

Features Dynamic Language Filtering: Implementación de filtrado por idioma a través de parámetros en la URL, permitiendo sesiones de práctica personalizadas.
=======
Este módulo complementa el diccionario de vocabulario mediante una interfaz de aprendizaje interactiva, permitiendo a los usuarios poner a prueba sus conocimientos de manera dinámica.

Features
Dynamic Language Filtering: Implementación de filtrado por idioma a través de parámetros en la URL, permitiendo sesiones de práctica personalizadas.
>>>>>>> efa5738a56b0e9ab7400ea5e372fbbd2097a2011

Session-Based Scoring: Sistema de puntuación persistente (+1 acierto, -1 fallo) utilizando django.contrib.sessions, lo que permite seguir el progreso sin necesidad de autenticación.

Randomized Learning Logic: Algoritmo que selecciona palabras de forma aleatoria de la base de datos para garantizar que cada sesión de estudio sea única.

Post/Redirect/Get Pattern: Implementación de redirecciones tras el envío de formularios para evitar el reenvío de datos al recargar y asegurar la integridad del puntaje.

State Management: Lógica inteligente de reinicio de puntuación que detecta cambios de idioma para mantener la coherencia en las métricas de aprendizaje.

UX-Focused Feedback: Sistema de mensajes temporales (Success/Error) integrados en el flujo de la sesión para retroalimentación inmediata del usuario.

<<<<<<< HEAD
Tech Stack Framework: Django 5.x
=======
Tech Stack
Framework: Django 5.x
>>>>>>> efa5738a56b0e9ab7400ea5e372fbbd2097a2011

Language: Python 3.x

Session Management: Django Session Engine

Frontend: Django Templates (HTML/CSS)

<<<<<<< HEAD
Setup & Installation El proceso de instalación es el mismo que en el módulo principal.
=======
Setup & Installation
El proceso de instalación es el mismo que en el módulo principal.
>>>>>>> efa5738a56b0e9ab7400ea5e372fbbd2097a2011

Activar Entorno Virtual: (Ver instrucciones de Intern 1)

Migrar la Base de Datos:

<<<<<<< HEAD
Bash python manage.py migrate Poblar Vocabulario: Es necesario añadir palabras desde el panel de administración o el formulario de vocabulario antes de iniciar el Quiz.

Project Structure (Quiz App) views.py: Manejo de la lógica de puntuación, control de sesiones y selección aleatoria de términos.
=======
Bash
python manage.py migrate
Poblar Vocabulario: Es necesario añadir palabras desde el panel de administración o el formulario de vocabulario antes de iniciar el Quiz.

Project Structure (Quiz App)
views.py: Manejo de la lógica de puntuación, control de sesiones y selección aleatoria de términos.
>>>>>>> efa5738a56b0e9ab7400ea5e372fbbd2097a2011

urls.py: Mapeo de rutas para la vista principal del Quiz.

templates/quiz/: Interfaz de usuario dinámica que muestra la palabra a traducir, el resultado del intento anterior y el marcador actual.

<<<<<<< HEAD
Usage Iniciar Práctica General: http://127.0.0.1:8000/quiz/
=======
Usage
Iniciar Práctica General: http://127.0.0.1:8000/quiz/
>>>>>>> efa5738a56b0e9ab7400ea5e372fbbd2097a2011

Práctica por Idioma Específico: http://127.0.0.1:8000/quiz/?language=ingles

Siguiente Palabra: Utiliza el botón "Siguiente" para cambiar de término manteniendo tu puntuación actual.
=======
# Language Learning Django App 🌍

A collaborative Django-based web application developed as part of an internship project. The app is designed to help users manage personal vocabulary and practice through interactive quizzes.

##  Vocabulary Module (Implemented by Intern 1)
This module serves as the core dictionary of the application, allowing users to store and organize words they are learning.

### Features
* **Data Persistence:** Implemented the `Word` model to store original terms, translations, and target languages.
* **Administrative Interface:** Fully configured Django Admin integration for easy database management.
* **Dynamic Word List:** Created a public-facing view that retrieves and displays all stored vocabulary entries.
* **User Input Handling:** Developed a `ModelForm` and a dedicated view to allow users to add new words directly from the browser.
* **Clean Architecture:** Implemented proper URL routing and template namespacing to ensure scalability and avoid conflicts.

##  Tech Stack
* **Framework:** Django 5.x
* **Language:** Python 3.x
* **Database:** SQLite (Development)
* **Version Control:** Git / GitHub

##  Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd language-learning-django-app
   ```

2. **Set up a Virtual Environment:**
```Windows
python -m venv venv
```
# Windows:
```Windows
.\venv\Scripts\activate
```

# macOS/Linux:
```bash
source venv/bin/activate
```
3. **Install Dependencies:**
```Windows
pip install django
```
4. **Initialize Database:**
```Windows
python manage.py makemigrations
python manage.py migrate
```
5. **Run the Application:**
``` Windows
python manage.py runserver
```
**Project Structure (Vocabulary App)**
models.py: Database schema for words.

forms.py: Logic for the vocabulary entry form.

views.py: Request handling for listing and adding words.

urls.py: App-specific URL mapping.

templates/vocabulary/: HTML templates (List and Add Word views).

**Usage**
Access the vocabulary list at: http://127.0.0.1:8000/vocabulary/

Add new words at: http://127.0.0.1:8000/vocabulary/add/

Manage data via the admin panel: http://127.0.0.1:8000/admin/



Developed by Daniel Márquez Quintero - Intern 1
>>>>>>> 60001d4ad1378faa05398c51c2ef972f7c18a2d5
