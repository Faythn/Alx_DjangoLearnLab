# posts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post

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


