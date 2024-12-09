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


class TokenPairSchema(Schema):
    access: str
    refresh: str


class RequestRestPasswordSchema(Schema):
    email: EmailStr
    username: str


class LoginSchema(Schema):
    username: str
    password: str


class ResetPasswordSchema(Schema):
    otp: str
    new_password: str
    new_password_repeat: str
