from ninja_jwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return dict(refresh=str(refresh), access=str(refresh.access_token))


def get_access_with_refresh(refresh_token):
    refresh = RefreshToken(refresh_token)
    return str(refresh.access_token)
