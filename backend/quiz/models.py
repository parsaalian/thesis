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
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    date = models.DateField()
    
    class Meta:
        unique_together = ('stock', 'pattern', 'date',)
