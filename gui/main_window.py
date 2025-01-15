import tkinter as tk
from tkinter import ttk
from .note_window import NoteWindow
from .widgets import NewNoteButton, DeleteNoteButton

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes App")
        self.root.geometry("500x500")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.new_note_button = NewNoteButton(self.notebook)
        self.new_note_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_note_button = DeleteNoteButton(self.notebook)
        self.delete_note_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.load_notes()

    def load_notes(self):
        # Funkcja do ładowania zapisanych notatek
        pass
