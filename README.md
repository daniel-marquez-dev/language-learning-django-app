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

2. **Set up a Virtual Environment:**
python -m venv venv

# Windows:
.\venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

3. **Install Dependencies:**
pip install django

4. **Initialize Database:**
python manage.py makemigrations
python manage.py migrate

5. **Run the Application:**
python manage.py runserver

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
