from django.urls import path

from myapp.views.CatalogView import CatalogView
from myapp.views.FolderView import FolderView
from myapp.views.FileView import FileView

urlpatterns = [
    path('catalog/', CatalogView.as_view()),
    path('catalog/<int:pk>/', FolderView.as_view()),
    path('catalog/file/', FileView.as_view())
]