from django.contrib import admin
from django.urls import path
from django.conf.urls.static  import static
from django.conf import settings
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products',include('products.urls', namespace="products")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
