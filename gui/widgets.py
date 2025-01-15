import tkinter as tk
from tkinter import ttk
from .note_window import NoteWindow

class NewNoteButton(ttk.Button):
    def __init__(self, notebook):
        super().__init__(text="New Note", command=self.add_note)
        self.notebook = notebook

    def add_note(self):
        NoteWindow(self.notebook)

class DeleteNoteButton(ttk.Button):
    def __init__(self, notebook):
        super().__init__(text="Delete", command=self.delete_note)
        self.notebook = notebook

    def delete_note(self):
        # Funkcja do usuwania notatki
        pass
