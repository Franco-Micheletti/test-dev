"""
Search URLs
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('search/type=<vehicle_type>&order_by=<order_by>',
         views.Search.as_view(), name='search_all_parameters'),
    path('search/type=<vehicle_type>',
         views.Search.as_view(), name='search_type_only'),
    path('search/order_by=<order_by>',
         views.Search.as_view(), name='search_order_by_only'),
    path('search/',
         views.Search.as_view(), name='search_with_no_parameters')
]

urlpatterns = format_suffix_patterns(urlpatterns)
