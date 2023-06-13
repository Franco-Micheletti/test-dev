"""
Search URLs
"""
from django.urls import path
from . import views

urlpatterns = [

    path('search/type=<vehicle_type>&order_by=<order_by>',
         views.SearchWithOrderBy.as_view()),
    path('search/type=<vehicle_type>', views.SearchWithOutOrderBy.as_view())
]
