# notes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),  # Default URL to list all notes
    path('note/<int:pk>/', views.note_detail, name='note_detail'),  # URL for viewing a note's details
    path('note/new/', views.note_create, name='note_create'),  # URL for creating a new note
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),  # URL for editing a note
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),  # URL for deleting a note

    path('bulletin/', views.bulletin_list, name='bulletin_list'),  # URL for listing all bulletin posts
    path('bulletin/<int:pk>/', views.bulletin_detail, name='bulletin_detail'),  # URL for viewing a post's details
    path('bulletin/new/', views.bulletin_create, name='bulletin_create'),  # URL for creating a new post
    path('bulletin/<int:pk>/edit/', views.bulletin_edit, name='bulletin_edit'),  # URL for editing a post
    path('bulletin/<int:pk>/delete/', views.bulletin_delete, name='bulletin_delete'),  # URL for deleting a post
]
