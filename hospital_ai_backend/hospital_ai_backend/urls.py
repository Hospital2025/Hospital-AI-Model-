# hospital_ai_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from resources.views import BedViewSet, EquipmentViewSet, StaffViewSet, MedicineViewSet, ShortagePredictionView

router = routers.DefaultRouter()
router.register(r'beds', BedViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'medicines', MedicineViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API endpoints available at /api/
      path('api/predict-shortage/', ShortagePredictionView.as_view(), name='predict-shortage'),
]

