from django.contrib import admin
from .models import SaleTransaction, SaleProduct
# Register your models here.



@admin.register(SaleTransaction)
class SaleTransactionAdmin(admin.ModelAdmin):
    pass



@admin.register(SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    pass


