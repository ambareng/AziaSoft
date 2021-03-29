from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import DriversEducationViewSet, MedicalProviderViewSet, MedicalTypeViewSet

router = DefaultRouter()
router.register('drivers_education', DriversEducationViewSet, basename='drivers_education')
router.register('medical_provider', MedicalProviderViewSet, basename='medical_provider')
router.register('medical_type', MedicalTypeViewSet, basename='medical_type')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
]
