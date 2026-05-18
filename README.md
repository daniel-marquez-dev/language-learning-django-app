<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
Quiz Module (Implemented by Intern 2)
=======
Quiz Module (Implemented by Intern 2) 
>>>>>>> a1cdbfe68f64b4803d3d1535d0431e37728da76c


This module complements the vocabulary dictionary through an interactive learning interface, allowing users to test their knowledge dynamically.

Features
Dynamic Language Filtering: Implementation of language filtering via URL parameters, enabling personalized practice sessions.

Session-Based Scoring: A persistent scoring system (+1 for correct, -1 for incorrect) using django.contrib.sessions, allowing progress tracking without requiring authentication.

Randomized Learning Logic: An algorithm that selects words randomly from the database to ensure every study session is unique.

Post/Redirect/Get Pattern: Implementation of form redirection to prevent data resubmission on page refresh and ensure score integrity.

State Management: Intelligent score-reset logic that detects language changes to maintain consistency in learning metrics.

UX-Focused Feedback: A system of temporary messages (Success/Error) integrated into the session flow for immediate user feedback.

Tech Stack
Framework: Django 5.x

Language: Python 3.x

Session Management: Django Session Engine

Frontend: Django Templates (HTML/CSS)

Setup & Installation
The installation process is the same as the main module.

Activate Virtual Environment: (See Intern 1 instructions).

Migrate the Database:

Bash
python manage.py migrate
Populate Vocabulary: You must add words via the admin panel or the vocabulary form before starting the Quiz.

Project Structure (Quiz App)
views.py: Handles scoring logic, session control, and random term selection.

urls.py: Route mapping for the main Quiz view.

templates/quiz/: Dynamic user interface showing the word to translate, the result of the previous attempt, and the current scoreboard.

Usage
Start General Practice: http://127.0.0.1:8000/quiz/

Practice by Specific Language: http://127.0.0.1:8000/quiz/?language=english

<<<<<<< HEAD
Siguiente Palabra: Utiliza el botón "Siguiente" para cambiar de término manteniendo tu puntuación actual.
=======
=======
>>>>>>> 401091808ac97fdfd6bb6efe23b31c7cea1597d8
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
<<<<<<< HEAD
>>>>>>> 60001d4ad1378faa05398c51c2ef972f7c18a2d5
=======
Next Word: Use the "Next" button to switch terms while maintaining your current score.
>>>>>>> a1cdbfe68f64b4803d3d1535d0431e37728da76c
=======
Quiz Module (Implemented by Intern 2) 


This module complements the vocabulary dictionary through an interactive learning interface, allowing users to test their knowledge dynamically.

Features
Dynamic Language Filtering: Implementation of language filtering via URL parameters, enabling personalized practice sessions.

Session-Based Scoring: A persistent scoring system (+1 for correct, -1 for incorrect) using django.contrib.sessions, allowing progress tracking without requiring authentication.

Randomized Learning Logic: An algorithm that selects words randomly from the database to ensure every study session is unique.

Post/Redirect/Get Pattern: Implementation of form redirection to prevent data resubmission on page refresh and ensure score integrity.

State Management: Intelligent score-reset logic that detects language changes to maintain consistency in learning metrics.

UX-Focused Feedback: A system of temporary messages (Success/Error) integrated into the session flow for immediate user feedback.

Tech Stack
Framework: Django 5.x

Language: Python 3.x

Session Management: Django Session Engine

Frontend: Django Templates (HTML/CSS)

Setup & Installation
The installation process is the same as the main module.

Activate Virtual Environment: (See Intern 1 instructions).

Migrate the Database:

Bash
python manage.py migrate
Populate Vocabulary: You must add words via the admin panel or the vocabulary form before starting the Quiz.

Project Structure (Quiz App)
views.py: Handles scoring logic, session control, and random term selection.

urls.py: Route mapping for the main Quiz view.

templates/quiz/: Dynamic user interface showing the word to translate, the result of the previous attempt, and the current scoreboard.

Usage
Start General Practice: http://127.0.0.1:8000/quiz/

Practice by Specific Language: http://127.0.0.1:8000/quiz/?language=english

Next Word: Use the "Next" button to switch terms while maintaining your current score.
>>>>>>> 401091808ac97fdfd6bb6efe23b31c7cea1597d8
