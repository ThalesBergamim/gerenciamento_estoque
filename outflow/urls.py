from django.urls import path
from . import views


urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', views.OutflowCreateView.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflow_detail'),
    path('api/v1/outflows/', views.OutflowCreateListAPIView.as_view(), name='outflow_create_list_api_view'),
    path('api/v1/outflows/<int:pk>/', views.OutflowDetailAPIView.as_view(), name='outflow_detail_api_view')
]
