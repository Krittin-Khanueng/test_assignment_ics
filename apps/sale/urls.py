from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('sale-transaction', views.SaleTransactionViewSet)
router.register('sale-product', views.SaleTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
