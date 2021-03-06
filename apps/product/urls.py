from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('size', views.SizeViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
