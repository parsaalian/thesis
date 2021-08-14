from django.db import models
from bourse_refs_api.models import Stock


class Pattern(models.Model):
    pattern_key = models.CharField(max_length=250, primary_key=True)

class PatternArticle(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    href = models.CharField(max_length=250, primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    body = models.TextField()


class PatternReference(models.Model):
    pattern_referrer = models.ForeignKey('Pattern', related_name='pattern_referrer', on_delete=models.CASCADE)
    pattern_referee = models.ForeignKey('Pattern', related_name='pattern_referee', on_delete=models.CASCADE)


class HistoricalPatternActionPoint(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    stock_id = models.BigIntegerField(default=0)
    date = models.DateField()
    value = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ('pattern', 'stock_id', 'date',)


class Question(models.Model):
    pass