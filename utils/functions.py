from rest_framework.authtoken.models import Token
from user.models import User


def get_token_for_user(user_id):
    """ Get token for User """

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return ''

    token, _ = Token.objects.get_or_create(user=user)

    return token.key
