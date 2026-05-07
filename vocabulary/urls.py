from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_list, name='word_list'),
    path('add/', views.add_word, name='add_word'),
]