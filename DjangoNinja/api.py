from ninja import NinjaAPI
from ninja_jwt.authentication import JWTAuth

api = NinjaAPI(auth=JWTAuth())

api.add_router("user-api", 'user.api.views.user_views.user_router', tags=["user-api"])
api.add_router("auth-api", 'user.api.views.auth_views.auth_router', tags=["auth-api"])
