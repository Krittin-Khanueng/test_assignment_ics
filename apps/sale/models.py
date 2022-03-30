import uuid

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.product.models import Product

User = get_user_model()


class SaleTransaction(models.Model):
    class STATUS(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, help_text='ผู้ที่ทำรายการสั่งซื้อ')
    address = models.TextField(help_text='ที่อยู่สำหรับจัดส่งสินค้า')
    phone = models.CharField(max_length=20, help_text='เบอร์โทรศัพท์สำหรับติดต่อกลับ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS.choices, default=STATUS.PENDING)
    pending_date = models.DateTimeField(null=True, blank=True, help_text='วันที่สั่งซื้อสินค้า')
    completed_date = models.DateTimeField(null=True, blank=True, help_text='วันที่สั่งซื้อสินค้าเสร็จสิ้น')
    cancelled_date = models.DateTimeField(null=True, blank=True, help_text='วันที่สั่งซื้อสินค้าถูกยกเลิก')

    @property
    def sale_product(self):
        return self.saleproduct_set.all()


class SaleProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, help_text='สินค้าที่สั่งซื้อ')
    amount = models.IntegerField(help_text='จำนวนสินค้าที่สั่งซื้อ')
    price = models.DecimalField(max_digits=4, decimal_places=2, help_text='ราคาสินค้าที่สั่งซื้อ')
    sale_transaction = models.ForeignKey(SaleTransaction, on_delete=models.CASCADE, null=True, blank=True,
                                         help_text='รายการสั่งซื้อสินค้า')
