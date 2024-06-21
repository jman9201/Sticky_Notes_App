from django.test import TestCase
from .models import Note, BulletinPost
from django.urls import reverse


class NoteModelTests(TestCase):
    """
    Test cases for the Note model.
    """

    def test_create_note(self):
        """
        Test the creation of a Note instance.
        """
        note = Note.objects.create(title="Test Note", content="Test Content")
        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.content, "Test Content")


class BulletinPostModelTests(TestCase):
    """
    Test cases for the BulletinPost model.
    """

    def test_create_post(self):
        """
        Test the creation of a BulletinPost instance.
        """
        post = BulletinPost.objects.create(
            title="Test Post",
            content="Test Content"
        )
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "Test Content")


class NoteViewTests(TestCase):
    """
    Test cases for the Note views.
    """

    def test_note_list_view(self):
        """
        Test the note list view.
        Ensure it returns a 200 status code and contains 'Notes'.
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Notes")

    def test_note_create_view(self):
        """
        Test the note creation view.
        Ensure it redirects to the detail view upon successful creation.
        """
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New Content'
        })
        # Redirects to detail view
        self.assertEqual(response.status_code, 302)


class BulletinPostViewTests(TestCase):
    """
    Test cases for the BulletinPost views.
    """

    def test_bulletin_list_view(self):
        """
        Test the bulletin list view.
        Ensure it returns a 200 status code and contains 'Bulletin'.
        """
        response = self.client.get(reverse('bulletin_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bulletin")

    def test_bulletin_create_view(self):
        """
        Test the bulletin post creation view.
        Ensure it redirects to the detail view upon successful creation.
        """
        response = self.client.post(reverse('bulletin_create'), {
            'title': 'New Post',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to detail view
