from django.contrib.auth import get_user_model
from ninja import ModelSchema, Schema


class UserInSchema(Schema):
    username: str
    password: str


class UserOutSchema(ModelSchema):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']
