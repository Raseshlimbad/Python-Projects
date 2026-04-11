# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List
# from database import notes_db

# app = FastAPI()

# class Note(BaseModel):
#     id: int
#     title: str
#     content: str

# # CREATE
# @app.post("/notes/")
# def create_note(note: Note):
#     notes_db.append(note)
#     return {"message": "Note created successfully", "note": note}

# # READ ALL
# @app.get("/notes/", response_model=List[Note])
# def get_all_notes():
#     return notes_db

# # READ ONE
# @app.get("/notes/{note_id}")
# def get_note(note_id: int):
#     for note in notes_db:
#         if note.id == note_id:
#             return note
#     raise HTTPException(status_code=404, detail="Note not found")

# # UPDATE
# @app.put("/notes/{note_id}")
# def update_note(note_id: int, updated_note: Note):
#     for i, note in enumerate(notes_db):
#         if note.id == note_id:
#             notes_db[i] = updated_note 
#             return {
#                 "message": "Note updated successfully",
#                 "note": updated_note
#             }
#     raise HTTPException(status_code=404, detail="Note not found")

# # DELETE
# @app.delete("/notes/{note_id}")
# def delete_note(note_id: int):
#     for i,note in enumerate(notes_db):
#         if note.id == note_id:
#             notes_db.pop(i)
#             return {"message": "Note deleted successfully"}
#     raise HTTPException(status_code=404, detail="Note not found")


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db
from models import NoteModel
from schemas import Note

app = FastAPI()

# Create tables
NoteModel.metadata.create_all(bind=engine)

# CREATE
@app.post("/notes/")
def create_note(note: Note, db: Session = Depends(get_db)):
    db_note = NoteModel(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# READ ALL
@app.get("/notes/", response_model=List[Note])
def get_notes(db: Session = Depends(get_db)):
    return db.query(NoteModel).all()

# READ ONE
@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Not found")
    return note

# UPDATE
@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note, db: Session = Depends(get_db)):
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Not found")

    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note

# DELETE
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(NoteModel).filter(NoteModel.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(note)
    db.commit()

    return {"message": "Deleted"}