from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from posts.models import Post
from posts.serializers import PostSerializer


class BoardList(generics.ListCreateAPIView):
    """
    List all boards, or create a new board.
    """
    model = Post
    serializer_class = PostSerializer

    def pre_save(self, obj):
        obj.author = self.request.user
        obj.nbr_tippers = len(obj._m2m_data['tippers'])


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a board instance.
    """
    model = Post
    serializer_class = PostSerializer

