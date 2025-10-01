# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, QRCodeViewSet, UserNFTViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'qr', QRCodeViewSet)
router.register(r'nft', UserNFTViewSet, basename='nft')

urlpatterns = [
    path('', include(router.urls)),
]
