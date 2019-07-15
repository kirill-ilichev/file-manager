from django.contrib import admin
from .models import Folder, File, User


class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'user')

class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'id', 'folder')

admin.site.register(Folder, FolderAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(User)