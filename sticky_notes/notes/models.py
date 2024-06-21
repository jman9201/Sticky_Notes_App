from django.db import models
from tinymce.models import HTMLField


class Note(models.Model):
    """
    A model representing a Note with a title and content.

    Attributes:
        title (str): The title of the note.
        content (HTMLField): The content of the note, stored as rich text.
        created_at (datetime): The date and time when the note was created.
        updated_at (datetime): The date and time when the note was last
        updated.
    """
    title = models.CharField(max_length=200, help_text="The title of the note")
    content = HTMLField(help_text="The content of the note, stored as rich text")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the note was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the note was last updated")

    def __str__(self):
        """
        String representation of the Note model, returning the note's title.
        """
        return self.title


class BulletinPost(models.Model):
    """
    A model representing a Bulletin Post with a title and content.

    Attributes:
        title (str): The title of the bulletin post.
        content (HTMLField): The content of the bulletin post, stored as rich
        text.created_at (datetime): The date and time when the bulletin post
        was created. updated_at (datetime): The date and time when the
        bulletin post was last updated.
    """
    title = models.CharField(max_length=200, help_text="The title of the bulletin post")
    content = HTMLField(help_text="The content of the bulletin post, stored as rich text")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the bulletin post was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the bulletin post was last updated")

    def __str__(self):
        """
        String representation of the BulletinPost model, returning the post's title.
        """
        return self.title
