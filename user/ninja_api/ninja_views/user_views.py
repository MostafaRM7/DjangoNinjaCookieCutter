from typing import List

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja import Router

from user.ninja_api.schemas import UserOutSchema, UserInSchema

user_router = Router()


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


@user_router.post("/users", response={200: UserOutSchema, 422: dict}, auth=None)
def create_user(request, payload: UserInSchema):
    user_exists = get_user_model().objects.filter(username=payload.username).exists()
    if user_exists:
        return 422, {"message": "User already exists"}
    user = get_user_model().objects.create_user(**payload.dict())
    return user



