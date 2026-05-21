from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.quiz_view, name='quiz'),
    path('quiz/check/', views.quiz_check, name='quiz_check'),
    path('quiz/next/', views.quiz_next, name='quiz_next'),
]