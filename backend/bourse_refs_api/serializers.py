from rest_framework.serializers import ModelSerializer

from .models import StockHistory


class StockHistorySerializer(ModelSerializer):
    class Meta:
        model = StockHistory
        fields = [
            'stock',
            'date',
            'max_price',
            'min_price',
            'last_price',
            'first_price',
            'value',
            'volume'
        ]