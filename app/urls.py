from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api/v1vschema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.home, name='home'),
    path('api/v1/', include('authentication.urls')),

    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('supplier.urls')),
    path('', include('inflows.urls')),
    path('', include('outflow.urls')),
    path('', include('product.urls')),

    path('admin/', admin.site.urls),
]
