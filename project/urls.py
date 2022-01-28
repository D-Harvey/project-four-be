from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients/', include('clients.urls')),
    path('api/auth/', include('jwt_auth.urls')),
    path('api/facebook/', include('facebook.urls')),
]
