from django.urls import path

from note.ninja_api.ninja_views import note_router

urlpatterns = [
    path("note-api", note_router.urls),
]
