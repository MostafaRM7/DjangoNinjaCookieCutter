from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja_jwt.tokens import RefreshToken

from user.ninja_api.schemas import TokenPairSchema, RequestRestPasswordSchema, LoginSchema, ResetPasswordSchema
from user.utils.auth import get_tokens_for_user, get_access_with_refresh, retrieve_user_id_with_otp, \
    validate_reset_password

auth_router = Router()


@auth_router.post("/login", response={200: TokenPairSchema, 422: dict}, auth=None)
def login(request, payload: LoginSchema):
    username = payload.username
    password = payload.password
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


@auth_router.post("logout/", response={200: dict, 422: dict})
def logout(request, refresh_token: str):
    try:
        refresh_token = RefreshToken(refresh_token)
        refresh_token.blacklist()
        return 200, {"message": "Logout successful"}
    except Exception as e:
        return 422, {"message": str(e)}


@auth_router.post("request-reset-password/", response={200: dict, 422: dict}, auth=None)
def request_reset_password(request, payload: RequestRestPasswordSchema):
    email = payload.email
    username = payload.username
    user = get_object_or_404(get_user_model(), email=email, username=username)
    otp = user.send_reset_password_email()
    return 200, {"message": otp}


@auth_router.post("reset-password/", response={200: dict, 422: dict}, auth=None)
def reset_password(request, payload: ResetPasswordSchema):
    otp = payload.otp
    new_password = payload.new_password
    new_password_repeat = payload.new_password_repeat
    user_id = retrieve_user_id_with_otp(otp)
    if user_id:
        user = get_user_model().objects.filter(id=user_id)
        if user.exists():
            is_password_valid = validate_reset_password(new_password, new_password_repeat)
            if is_password_valid:
                user = user.first()
                user.set_password(new_password)
                user.save()
                return 200, {"message": "New password set sucssessfuly"}
            else:
                return 422, {"message": "Invalid password"}
    return 422, {"message": "Wrong OTP"}
