from django.contrib.auth.models import User
from django.db import models
from quiz.models import Pattern


class LeitnerBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    box_number = models.IntegerField()
