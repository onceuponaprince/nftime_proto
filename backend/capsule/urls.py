from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SmartContractViewSet, MemoryViewSet

router = DefaultRouter()
router.register(r'capsule', SmartContractViewSet)
router.register(r'memory', MemoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]