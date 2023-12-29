from django.shortcuts import render, HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import Post
from home.serializers import PostSerializer


class Base(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data
            Post.objects.create(name=data['name'], author=request.user)
            return Response('added')
        return Response('not add')

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
        return Response(serializer.data)


def bet(request):
    return HttpResponse("ok")
