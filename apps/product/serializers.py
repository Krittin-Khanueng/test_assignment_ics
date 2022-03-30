from rest_framework import serializers

from apps.product.models import Category, Size, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField(read_only=True)

    def get_gender(self, obj):
        return obj.get_gender_display()

    class Meta:
        model = Size
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    size = SizeSerializer()

    class Meta:
        model = Product
        fields = '__all__'
