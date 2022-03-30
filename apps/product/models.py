import uuid

from django.db import models


# Create your models here.


class Size(models.Model):
    class GENDERS(models.TextChoices):
        MAN = "1", "MAN"
        FEMALE = "2", "FEMALE"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.CharField(max_length=10, help_text="ไซส์สินค้า")
    gender = models.CharField(max_length=2, choices=GENDERS.choices, help_text="เพศ")
    shoulder_width = models.DecimalField(max_digits=4, decimal_places=2, help_text="ความกว้างของหัวไหล่(cm)")
    sleeve_length = models.DecimalField(max_digits=4, decimal_places=2, help_text="ความยาวของแขนเสื้อ(cm)")
    back_length = models.DecimalField(max_digits=4, decimal_places=2, help_text="ความยาวด้านหลังเสื้อ(cm)")
    neck = models.DecimalField(max_digits=4, decimal_places=2, help_text="รอบคอ(cm)")

    def __str__(self):
        return f"{self.size} {self.get_gender_display()}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, help_text="ชื่อหมวดหมู่สินค้า")

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, help_text="ชื่อสินค้า")
    price = models.DecimalField(max_digits=4, decimal_places=2, help_text="ราคาสินค้า")
    description = models.TextField(help_text="รายละเอียดสินค้า")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True, help_text="ไซส์เสื้อ")
    amount = models.IntegerField(help_text="จำนวนสินค้า")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, help_text="หมวดหมู่สินค้า")
    is_active = models.BooleanField(default=True, help_text="สถานะสินค้า")
