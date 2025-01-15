import json

def save_note_to_file(title, content):
    notes = load_notes_from_file()
    notes[title] = content.strip()
    with open("data/notes.json", "w") as f:
           with open("data/notes.json", "w") as f:
           json.dump(notes, f)

   def load_notes_from_file():
       try:
           with open("data/notes.json", "r") as f:
               notes = json.load(f)
       except FileNotFoundError:
           notes = {}
       return notes
