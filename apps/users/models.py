import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authentication import TokenAuthentication


# Create your models here.


class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'


class CustomUser(AbstractUser):
    """
    Custom User which extends AbstractUser
    Add add UUID
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, help_text='วัน-เวลาสร้าง')
    updated = models.DateTimeField(auto_now=True, help_text='วัน-เวลาแก้ไขล่าสุด')
    address = models.TextField(blank=True, null=True, help_text='ที่อยู่สำหรับจัดส่งสินค้า')

    @property
    def display_name(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        else:
            return self.username

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
