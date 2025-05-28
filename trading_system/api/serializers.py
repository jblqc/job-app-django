from rest_framework import serializers
from .models import Stock, Order

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'symbol', 'company_name', 'price']

class OrderSerializer(serializers.ModelSerializer):
    stock_id = serializers.PrimaryKeyRelatedField(
        queryset=Stock.objects.all(),
        source='stock'
    )
    stock = StockSerializer(read_only=True)

    created_at = serializers.DateTimeField(read_only=True)  # renamed field

    class Meta:
        model = Order
        fields = ['id', 'stock_id', 'stock', 'quantity', 'price', 'created_at']
        read_only_fields = ['id', 'stock', 'created_at']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        # Remove 'stock' field on input to avoid it showing in POST body
        if request and request.method in ['POST', 'PUT', 'PATCH']:
            fields.pop('stock', None)
        return fields

    def create(self, validated_data):
        if 'price' not in validated_data or validated_data['price'] is None:
            validated_data['price'] = validated_data['stock'].price
        return super().create(validated_data)
