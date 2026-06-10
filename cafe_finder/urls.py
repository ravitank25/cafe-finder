from django.contrib import admin
from django.urls import path
from cafes import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("add-cafe/", views.add_cafe, name="add_cafe"),
    path("cafe/<int:id>/", views.cafe_detail, name="cafe_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
