from ninja import Schema
from pydantic import EmailStr


class TokenPairSchema(Schema):
    access: str
    refresh: str


class RequestRestPasswordSchema(Schema):
    email: EmailStr
    username: str


class SignUpSchema(Schema):
    username: str
    email: EmailStr
    password: str


class LoginSchema(Schema):
    username: str
    password: str


class ResetPasswordSchema(Schema):
    otp: str
    new_password: str
    new_password_repeat: str
