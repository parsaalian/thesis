from rest_framework.serializers import ModelSerializer

from .models import PatternArticle, HistoricalPatternActionPoint

class HistoricalPatternActionPointSerializer(ModelSerializer):
    class Meta:
        model = HistoricalPatternActionPoint
        fields = ['pattern', 'stock_id', 'date']


class PatternArticleSerializer(ModelSerializer):
    class Meta:
        model = PatternArticle
        fields = ['href', 'title', 'title', 'author', 'body']