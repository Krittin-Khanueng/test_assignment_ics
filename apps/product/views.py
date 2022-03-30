from django.shortcuts import render
from rest_framework import viewsets

from .models import Product, Category, Size
from .serializers import ProductSerializer, CategorySerializer, SizeSerializer
from .filtersets import ProductFilterSet


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilterSet

class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
