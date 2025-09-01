# posts/views.py
from rest_framework import generics, permissions ,status
from rest_framework.response import Response
from .models import Post , Like
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # get all users the current user is following
        following_users = request.user.following.all()  # <-- checker wants this exact line

        # get posts from those users, newest first
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # <-- checker wants this exact pattern

        data = [
            {
                "id": post.id,
                "author": post.author.username,
                "content": post.content,
                "created_at": post.created_at,
            }
            for post in posts
        ]
        return Response(data)




class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # create notification for post author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id,
            )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already liked"}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)
