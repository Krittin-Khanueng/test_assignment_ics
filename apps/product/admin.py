from django.contrib import admin
from .models import Product, Size, Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass



@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass