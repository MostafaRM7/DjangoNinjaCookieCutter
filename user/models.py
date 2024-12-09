from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache

from user.utils.auth import generate_otp


class User(AbstractUser):

    def send_reset_password_email(self):
        otp = generate_otp(5)
        cache.set(str(otp), str(self.id), timeout=settings.USER_RESET_PASSWORD_OTP_TIMEOUT)
        return otp
