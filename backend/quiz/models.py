from django.db import models


class Pattern(models.Model):
    pattern_key = models.CharField(max_length=250, primary_key=True)
    pattern_description = models.TextField()


class PatternArticle(models.Model):
    href = models.CharField(max_length=250, primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    body = models.TextField()


class PatternReference(models.Model):
    Referrer = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    Referee = models.ForeignKey(Pattern, on_delete=models.CASCADE)
