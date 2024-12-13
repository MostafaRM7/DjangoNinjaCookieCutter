from random import randint

from django.core.cache import cache
from ninja_jwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return dict(refresh=str(refresh), access=str(refresh.access_token))


def get_access_with_refresh(refresh_token):
    refresh = RefreshToken(refresh_token)
    return str(refresh.access_token)


def generate_otp(length):
    return randint(10 ** (length - 1), 10 ** length - 1)


def retrieve_user_id_with_otp(otp):
    user_id = cache.get(otp)
    if user_id:
        cache.delete(otp)
    return user_id


def validate_reset_password(new_password, new_password_repeat):
    return new_password == new_password_repeat
