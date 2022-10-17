from feed.models import PostLike
from accounts.models import User


def get_post_likes():
    return PostLike.objects.all()


def get_users():
    return User.objects.all()