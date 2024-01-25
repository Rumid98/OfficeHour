from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config.views import index, home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("", index),
    path("home/", home)
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
