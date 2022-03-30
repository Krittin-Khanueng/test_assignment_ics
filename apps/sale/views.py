from django.shortcuts import render
from rest_framework import viewsets

from .models import SaleTransaction, SaleProduct
from .serializers import SaleTransactionSerializer, SaleProductSerializer


class SaleTransactionViewSet(viewsets.ModelViewSet):
    queryset = SaleTransaction.objects.all()
    serializer_class = SaleTransactionSerializer


class SaleProductViewSet(viewsets.ModelViewSet):
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer
