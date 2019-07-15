from django.conf import settings
import jwt
from django.http import JsonResponse
from myapp.serializers import FolderSerializer
from myapp.models import User, Folder
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from myapp.helpers.catalog import get_catalog


class CatalogView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = jwt.decode(request.META['HTTP_AUTHORIZATION'][7:], settings.SECRET_KEY)
        folders = Folder.objects.filter(user__email=user['email'])

        if list(folders) == []:
            root_folder = {
                'name': f'{user["email"]} root folder ',
                'user': user['user_id']
            }
            serializer = FolderSerializer(data=root_folder)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        root_folder = Folder.objects.filter(user__email=user['email']).order_by('id')[0]
        return JsonResponse(get_catalog(user, root_folder))