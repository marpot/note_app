import tkinter as tk
from tkinter import ttk
from utils.file_operations import save_note_to_file

class NoteWindow:
    def __init__(self, notebook, title="New Note"):
        self.notebook = notebook
        self.title = title
        self.note_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.note_frame, text=self.title)

        self.title_label = ttk.Label(self.note_frame, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.title_entry = ttk.Entry(self.note_frame, width=40)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.content_label = ttk.Label(self.note_frame, text="Content:")
        self.content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.content_entry = tk.Text(self.note_frame, width=40, height=10)
        self.content_entry.grid(row=1, column=1, padx=10, pady=10)

        self.save_button = ttk.Button(self.note_frame, text="Save", command=self.save_note)
        self.save_button.grid(row=2, column=1, padx=10, pady=10)

    def save_note(self):
        title = self.title_entry.get()
        content = self.content_entry.get("1.0", tk.END)
        save_note_to_file(title, content)
        # Dodatkowe operacje po zapisaniu notatki
