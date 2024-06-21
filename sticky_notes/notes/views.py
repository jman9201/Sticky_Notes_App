from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, BulletinPost
from .forms import NoteForm, BulletinPostForm


def note_list(request):
    """
    View to list all notes
    """
    notes = Note.objects.all()  # Retrieve all notes from the database
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_detail(request, pk):
    """
    View to show the details of a single note
    """
    note = get_object_or_404(Note, pk=pk)  # Retrieve a specific note by primary key
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    """
    View to create a new note
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)  # Redirect to the note's detail view
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_edit(request, pk):
    """
    View to edit an existing note
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)  # Redirect to the note's detail view
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    """
    View to delete a note
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()  # Delete the note
        return redirect('note_list')  # Redirect to the list of notes
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


def bulletin_list(request):
    """
    View to list all bulletin posts
    """
    posts = BulletinPost.objects.all()  # Retrieve all bulletin posts from the database
    return render(request, 'notes/bulletin_list.html', {'posts': posts})


def bulletin_detail(request, pk):
    """
    View to show the details of a single bulletin post
    """
    post = get_object_or_404(BulletinPost, pk=pk)  # Retrieve a specific post by primary key
    return render(request, 'notes/bulletin_detail.html', {'post': post})


def bulletin_create(request):
    """
    View to create a new bulletin post
    """
    if request.method == "POST":
        form = BulletinPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('bulletin_detail', pk=post.pk)  # Redirect to the post's detail view
    else:
        form = BulletinPostForm()
    return render(request, 'notes/bulletin_form.html', {'form': form})


def bulletin_edit(request, pk):
    """
    View to edit an existing bulletin post
    """
    post = get_object_or_404(BulletinPost, pk=pk)
    if request.method == "POST":
        form = BulletinPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('bulletin_detail', pk=post.pk)  # Redirect to the post's detail view
    else:
        form = BulletinPostForm(instance=post)
    return render(request, 'notes/bulletin_form.html', {'form': form})


def bulletin_delete(request, pk):
    """
    View to delete a bulletin post
    """
    post = get_object_or_404(BulletinPost, pk=pk)
    if request.method == "POST":
        post.delete()  # Delete the post
        return redirect('bulletin_list')  # Redirect to the list of bulletin posts
    return render(request, 'notes/bulletin_confirm_delete.html', {'post': post})
