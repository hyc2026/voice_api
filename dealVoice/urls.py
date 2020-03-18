from django.urls import path
from . import views, word2voice, voice2word

urlpatterns = [
    path('word2voice/', word2voice.word2voice, name = 'word2voice'),
    path('voice2word/', voice2word.voice2word, name = 'voice2word')
]
