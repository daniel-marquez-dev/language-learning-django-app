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
