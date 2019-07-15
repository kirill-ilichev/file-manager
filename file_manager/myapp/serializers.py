from rest_framework import serializers
from django.contrib.auth import get_user_model
from myapp.models import Folder, File

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}, }


class FolderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Folder
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = "__all__"