from typing import List

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja import Router

from user.ninja_api.schemas import UserOutSchema, UserInSchema
from user.utils.auth import get_tokens_for_user, get_access_with_refresh

user_router = Router()
auth_router = Router()


@user_router.get("/users/me", response=UserOutSchema)
def retrieve_current_user(request):
    return request.user


@user_router.get("/users", response=List[UserOutSchema])
def list_users(request):
    return get_user_model().objects.all()


@user_router.get("/users/{user_id}", response=UserOutSchema)
def retrieve_user(request, user_id: int):
    user = get_object_or_404(get_user_model(), id=user_id)
    return user


@user_router.post("/users", response={200: UserOutSchema, 422: dict})
def create_user(request, payload: UserInSchema):
    user_exists = get_user_model().objects.filter(username=payload.username).exists()
    if user_exists:
        return 422, {"message": "User already exists"}
    user = get_user_model().objects.create_user(**payload.dict())
    return user


@auth_router.post("/login", response={200: dict, 422: dict}, auth=None)
def login(request, username: str, password: str):
    user = get_object_or_404(get_user_model(), username=username)
    if not user.check_password(password):
        return 422, {"message": "Invalid credentials"}
    return get_tokens_for_user(user)


@auth_router.post("/refresh", response={200: dict, 422: dict}, auth=None)
def refresh(request, refresh_token: str):
    try:
        return {"access": get_access_with_refresh(refresh_token)}
    except Exception as e:
        return 422, {"message": str(e)}
