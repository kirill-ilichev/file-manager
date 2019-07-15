from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import jwt
from django.conf import settings
from django.http import JsonResponse
from myapp.models import Folder
from myapp.serializers import FileSerializer
from rest_framework import status
from rest_framework.response import Response

class FileView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = jwt.decode(request.META['HTTP_AUTHORIZATION'][7:], settings.SECRET_KEY)
        root_folder = Folder.objects.filter(id=request.data['parentID'])[0]

        if root_folder.user.id != user['user_id']:
            return Response(status=status.HTTP_403_FORBIDDEN)

        files = dict(request.data)['file']
        file_info = {
            'parentID': request.data['parentID'],
            'files': []
        }
        for file in files:
            serializer = FileSerializer(data={
                'folder': request.data['parentID'],
                'file': file
            })

            serializer.is_valid(raise_exception=True)
            serializer.save()

            file_info['files'].append({
                'url': serializer.data['file'],
                'id': serializer.data['id'],
                'name': serializer.data['file'][serializer.data['file'].rfind('/')+1:]
            })

        return JsonResponse(file_info)