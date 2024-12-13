from django.contrib.auth import get_user_model
from ninja import ModelSchema, Schema
from pydantic import EmailStr


class UserInSchema(Schema):
    username: str
    password: str
    email: EmailStr


class UserOutSchema(ModelSchema):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']
