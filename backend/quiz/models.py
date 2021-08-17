from django.contrib.auth.models import User
from django.db import models


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


class PatternStatistics(models.Model):
    pattern = models.ForeignKey('Pattern', on_delete=models.CASCADE)
    value = models.IntegerField()
    count = models.IntegerField()
    
    change_mean = models.FloatField()
    change_std = models.FloatField()
    change_min = models.FloatField()
    change_25 = models.FloatField()
    change_50 = models.FloatField()
    change_75 = models.FloatField()
    change_max = models.FloatField()
    
    time_mean = models.IntegerField()
    time_std = models.IntegerField()
    time_min = models.IntegerField()
    time_25 = models.IntegerField()
    time_50 = models.IntegerField()
    time_75 = models.IntegerField()
    time_max = models.IntegerField()
    
    positive_rate = models.FloatField()
    
    class Meta:
        unique_together = ('pattern', 'value',)


class Question(models.Model):
    pass


class LeitnerBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    box_number = models.IntegerField()
