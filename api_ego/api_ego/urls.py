"""
URL configuration for api_ego project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    # Schema generator
    path('openapi', get_schema_view(
        title="Your Project",
        description="BACKEND API - EGO",
        version="3.0.0"
    ), name='openapi-schema'),
    # Swagger UI
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    # Admin
    path('admin/', admin.site.urls),
    # Product
    path('', include('product.urls')),
    # Search
    path('', include('search.urls'))
]
