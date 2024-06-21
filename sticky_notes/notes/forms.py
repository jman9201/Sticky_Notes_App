from django import forms
from .models import Note, BulletinPost
from tinymce.widgets import TinyMCE


class NoteForm(forms.ModelForm):
    """
    A form for creating and updating Note instances.

    Fields:
        title (CharField): The title of the note.
        content (CharField): The content of the note, using the TinyMCE
        widget for rich text editing.
    """
    content = forms.CharField(
        widget=TinyMCE(), help_text="The content of the note, using the TinyMCE widget for rich text editing")

    class Meta:
        model = Note
        fields = ['title', 'content']
        help_texts = {
            'title': 'The title of the note',
        }


class BulletinPostForm(forms.ModelForm):
    """
    A form for creating and updating BulletinPost instances.

    Fields:
        title (CharField): The title of the bulletin post.
        content (CharField): The content of the bulletin post, using the
        TinyMCE widget for rich text editing.
    """
    content = forms.CharField(widget=TinyMCE(), help_text="The content of the bulletin post, using the TinyMCE widget for rich text editing")

    class Meta:
        model = BulletinPost
        fields = ['title', 'content']
        help_texts = {
            'title': 'The title of the bulletin post',
        }
