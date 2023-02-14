from notes_app import NotesApp


def test_add_note():
    notes = NotesApp()
    result = notes.add_note("Test note 1")
    assert result == "Note added successfully"
    assert len(notes.notes_list) == 1
    assert notes.notes_list[0].content == "Test note 1"


def test_get_note():
    notes = NotesApp()
    notes.add_note("Test note 1")
    result = notes.get_note(0)
    assert result == "Test note 1"


def test_get_note_index_error():
    notes = NotesApp()
    result = notes.get_note(0)
    assert result == "Index out of range"


def test_edit_note():
    notes = NotesApp()
    notes.add_note("Test note 1")
    notes.edit_note(0, "Test note 1 edited")
    result = notes.get_note(0)
    assert result == "Test note 1 edited"


def test_edit_note_index_error():
    notes = NotesApp()
    result = notes.edit_note(0, "Test note 1 edited")
    assert result == "Index out of range"
