from django.contrib import admin
from django.urls import path, include

from myapp.views.CreateUserView import CreateUserView
from myapp.views.authenticate_user import authenticate_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/login/', authenticate_user),
    path('api/v1/auth/registration/', CreateUserView.as_view()),
    path('api/v1/', include('myapp.urls'))
]