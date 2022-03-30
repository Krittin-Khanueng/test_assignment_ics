from rest_framework import serializers

from apps.sale.models import SaleProduct, SaleTransaction


class SaleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = '__all__'


class SaleTransactionSerializer(serializers.ModelSerializer):
    sale_product = SaleProductSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        sale_product = validated_data.pop('sale_product')
        sale_transaction = super().create(validated_data)
        for product in sale_product:
            SaleProduct.objects.create(
                **{
                    'sale_transaction': sale_transaction,
                    **product
                }
            )
        return sale_transaction

    class Meta:
        model = SaleTransaction
        fields = '__all__'
