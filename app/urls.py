from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('supplier.urls')),
    path('', include('inflows.urls')),
    path('', include('outflow.urls')),
    path('', include('product.urls'))
]
