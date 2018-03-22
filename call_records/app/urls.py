"""
URL Configuration for app
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from app import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'call-record', views.CallRecordViewSet)
router.register(r'config-price', views.ConfigPriceViewSet)
router.register(r'bill', views.BillViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^$', views.IndexViewSet.as_view({'get': 'list'})),
    url(r'^docs/', include_docs_urls(title='REST API for Call Records')),
    url(r'^', include(router.urls)),
]
