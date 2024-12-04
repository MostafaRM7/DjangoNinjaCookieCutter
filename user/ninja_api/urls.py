from django.urls import path
from user.ninja_api.ninja_views import user_router

urlpatterns = [
    path("", user_router.urls),
]
