from datetime import datetime

from ninja import ModelSchema, Schema

from note.models import Note


class NoteInSchema(Schema):
    title: str
    content: str
    owner_id: int
    created_at: datetime


class NoteOutSchema(ModelSchema):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "owner"]
        read_only = ["id", "created_at"]
