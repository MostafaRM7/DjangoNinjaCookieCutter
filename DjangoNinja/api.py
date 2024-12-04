from ninja import NinjaAPI
from ninja_jwt.authentication import JWTAuth

api = NinjaAPI(auth=JWTAuth())

api.add_router("user-api", 'user.ninja_api.ninja_views.user_router', tags=["user-api"])
api.add_router("note-api", 'note.ninja_api.ninja_views.note_router', tags=["note-api"])
api.add_router("auth-api", 'user.ninja_api.ninja_views.auth_router', tags=["auth-api"])
