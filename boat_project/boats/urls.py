from django.urls import path, include
from boats import views as boats_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', boats_views.index, name='boats_home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
