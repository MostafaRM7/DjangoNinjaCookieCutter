from typing import List

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja import Router
from note.models import Note
from note.ninja_api.schemas import NoteInSchema, NoteOutSchema

note_router = Router()


@note_router.get("/notes", response=List[NoteOutSchema])
def list_notes(request):
    return Note.objects.all()


@note_router.get("/notes/{note_id}", response=NoteOutSchema)
def retrieve_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    return note


@note_router.post("/notes", response=NoteOutSchema)
def create_notes(request, payload: NoteInSchema):
    data = payload.dict()
    owner_id = data.pop("owner_id")
    owner = get_object_or_404(get_user_model(), id=owner_id)
    data["owner"] = owner
    note = Note.objects.create(**data)
    return note


@note_router.patch("/notes/{note_id}", response=NoteOutSchema)
def update_notes(request, note_id: int, payload: NoteInSchema):
    note = get_object_or_404(Note, id=note_id)
    for attr, value in payload.dict().items():
        setattr(note, attr, value)
    note.save()
    return note
