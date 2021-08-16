from random import choice
from .models import Pattern, HistoricalPatternActionPoint


def get_random_action_point():
    pattern = choice(Pattern.objects.all())
    action_point = choice(HistoricalPatternActionPoint.objects.filter(pattern=pattern))
    return action_point