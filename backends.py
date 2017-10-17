from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


def get_user(email, queryset=None):
    """
    Return the user with given email address.
    Note that email address matches are case-insensitive.
    """
    if queryset is None:
        queryset = User.objects

    result = queryset.filter(email=email)
    if result:
        return result[0]

    return None


class EmailAuthBackend(ModelBackend):
    """
    Allow users to log in with their email address
    """
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = get_user(email)
            if user and user.check_password(password):
                return user

            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
