from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, PhotoViewSet, login_view

router = routers.DefaultRouter()
router.register(r'user', PhotoViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view)
]