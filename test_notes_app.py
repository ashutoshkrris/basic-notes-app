import pytest

from notes_app import NotesApp


@pytest.fixture
def app_without_notes():
    app = NotesApp()
    return app


@pytest.fixture
def app_with_notes():
    app = NotesApp()
    app.add_note("Test note 1")
    app.add_note("Test note 2")
    return app


def test_add_note():
    notes = NotesApp()
    result = notes.add_note("Test note 1")
    assert result == "Note added successfully"
    assert len(notes.notes_list) == 1
    assert notes.notes_list[0].content == "Test note 1"


def test_get_note(app_with_notes):
    result = app_with_notes.get_note(0)
    assert result == "Test note 1"


def test_get_note_index_error(app_without_notes):
    result = app_without_notes.get_note(0)
    assert result == "Index out of range"


def test_edit_note(app_with_notes):
    app_with_notes.edit_note(0, "Test note 1 edited")
    result = app_with_notes.get_note(0)
    assert result == "Test note 1 edited"


def test_edit_note_index_error(app_without_notes):
    result = app_without_notes.edit_note(0, "Test note 1 edited")
    assert result == "Index out of range"
