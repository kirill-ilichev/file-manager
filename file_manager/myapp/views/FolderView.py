from django.conf import settings
from django.http import JsonResponse
import jwt

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from myapp.serializers import FolderSerializer
from myapp.models import Folder
from myapp.helpers.catalog import get_catalog

class FolderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = jwt.decode(request.META['HTTP_AUTHORIZATION'][7:], settings.SECRET_KEY)
        root_folder = Folder.objects.filter(id=pk)[0]

        if root_folder.user.id != user['user_id']:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return JsonResponse(get_catalog(user, root_folder))

    def post(self, request, pk):
        user = jwt.decode(request.META['HTTP_AUTHORIZATION'][7:], settings.SECRET_KEY)
        root_folder = Folder.objects.filter(id=pk)[0]

        if root_folder.user.id != user['user_id']:
            return Response(status=status.HTTP_403_FORBIDDEN)

        root_folder = {
            'name': request.data['name'],
            'user': user['user_id'],
            'parentID': pk
        }
        serializer = FolderSerializer(data=root_folder)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        root_folder.pop('user')
        return JsonResponse(root_folder)
