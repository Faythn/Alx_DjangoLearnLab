from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import User


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target = get_object_or_404(User, pk=user_id)
    if target == request.user:
        return Response({"detail": "You cannot follow yourself."},
                        status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(target)
    return Response(
        {
            "detail": f"You are now following {target.username}.",
            "following_count": request.user.following.count(),
            "target_followers": target.followers.count(),
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target = get_object_or_404(User, pk=user_id)
    if target == request.user:
        return Response({"detail": "You cannot unfollow yourself."},
                        status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(target)
    return Response(
        {
            "detail": f"You unfollowed {target.username}.",
            "following_count": request.user.following.count(),
            "target_followers": target.followers.count(),
        },
        status=status.HTTP_200_OK,
    )

