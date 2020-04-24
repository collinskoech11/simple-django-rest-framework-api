from django.urls import path
from .views import NoteApi

urlpatterns = [
    path('api/notes', NoteApi.as_view()),
]
