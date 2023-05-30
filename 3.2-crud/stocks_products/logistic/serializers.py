from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    
    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        for stock_products in positions:
            stock_product = StockProduct(stock=stock, 
                                        product=stock_products['product'],
                                        quantity=stock_products['quantity'],
                                        price=stock_products['price'])
            stock_product.save()

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        for stock_products in positions:
            stock_product = StockProduct.objects.update_or_create(stock=stock, 
                                                                  product=stock_products['product'], 
                                                                  defaults=stock_products)

        return stock
