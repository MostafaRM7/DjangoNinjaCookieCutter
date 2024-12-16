from typing import List

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja import Form
from ninja.files import UploadedFile
from ninja.pagination import RouterPaginated

from DjangoNinja.permissions import guard
from user.api.exceptions import USER_EXISTS
from user.api.permissions.user_permissions import user_list_create_permission, user_detail_permission
from user.api.schemas.user_schemas import UserOutSchema, UserInSchema

user_router = RouterPaginated()


@user_router.get("/users/me", response=UserOutSchema)
def retrieve_current_user(request):
    return request.user


@user_router.get("/users", response={200: List[UserOutSchema], 403: dict})
@guard([user_list_create_permission])
def list_users(request):
    return get_user_model().objects.all()


@user_router.get("/users/{user_id}", response={200: UserOutSchema, 403: dict})
@guard([user_detail_permission])
def retrieve_user(request, user_id: int):
    user = get_object_or_404(get_user_model(), id=user_id)
    return user


@user_router.post("/users", response={200: UserOutSchema, 422: dict, 403: dict})
@guard([user_list_create_permission])
def create_user(request, payload: Form[UserInSchema], avatar: UploadedFile = None):
    user_exists = get_user_model().objects.filter(username=payload.username).exists()
    if user_exists:
        return USER_EXISTS
    user = get_user_model().objects.create_user(**payload.dict(), avatar=avatar)
    return user
