from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from social_network import settings
from .yasg import urlpatterns as doc_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('feed/', include('feed.urls')),
    path('analytics/', include('analytics.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += doc_urlpatterns