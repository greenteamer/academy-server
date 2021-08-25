from project.settings import STATIC_URL, STATIC_ROOT
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("", include("main.urls")),
    path("admin/", admin.site.urls),
] + static(STATIC_URL, document_root=STATIC_ROOT)
