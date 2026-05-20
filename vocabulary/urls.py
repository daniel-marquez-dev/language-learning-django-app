from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('word_list/', views.word_list, name='word_list'),
    path('add-word/', views.add_word, name='add_word'),
    path('add-language/', views.add_language, name='add_language'),
]