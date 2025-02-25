from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('supplier.urls')),
    path('', include('inflows.urls')),
    path('', include('outflow.urls')),
    path('', include('product.urls'))
]
