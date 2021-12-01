from django.contrib import admin
from django.urls import path
from django.conf.urls.static  import static
from django.conf import settings
from django.urls.conf import include
from products import views_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products',include('products.urls', namespace="products")),
    path("users/login",views_users.login_v,name='login' ),
    path("users/logout",views_users.logout_v,name='logout' ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
