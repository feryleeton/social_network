from django.shortcuts import get_object_or_404

from accounts.models import User
from feed.models import Post, PostLike


def get_users():
    return User.objects.all()


def get_posts():
    return Post.objects.all()


def like_post(request, pk):
    """
    Creates like object for specific user and post in database
    :param request: request object
    :param pk: pk of the post to like
    :return: total likes count for given post
    """
    user = request.user
    post = get_object_or_404(Post, pk=pk)

    if PostLike.objects.filter(post=post, user=user).exists():
        PostLike.objects.filter(post=post, user=user).delete()
    else:
        PostLike.objects.create(
            post=post,
            user=user
        )

    total_likes_count = PostLike.objects.filter(
        post=post
    ).count()

    return total_likes_count