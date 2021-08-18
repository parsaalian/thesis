import numpy as np
from random import choice
from dateutil.relativedelta import relativedelta
from django.db.models import Max

from bourse_refs_api.models import StockHistory
from .trend import trend
from ..models import Pattern, HistoricalPatternActionPoint, LeitnerBox


def get_random_action_point():
    pattern = choice(Pattern.objects.all())
    action_point = choice(HistoricalPatternActionPoint.objects.filter(pattern=pattern))
    return action_point


def identify_question(pattern, wrong_choices_count):
    patterns = list(Pattern.objects.all())
    patterns = list(filter(lambda x: x != pattern, patterns))
    other_choices = np.random.choice(patterns, wrong_choices_count, replace=False)
    choices = np.random.permutation([pattern, *other_choices]),
    return {
        'prompt': 'Which pattern is seen at the end of the chart?',
        'choices': choices,
        'answer': choices.index(pattern)
    }


def predict_question(pattern):
    history = StockHistory.objects.filter(
        stock_id=pattern.stock_id,
        date__gte=pattern.date - relativedelta(days=14),
        date__lte=pattern.date + relativedelta(days=60)
    )
    pattern_future_trend = trend(history, pattern, ma=14)
    return {
        'prompt': 'What will be the trend after this point?',
        'choices': ['Bullish', 'Bearish'],
        'answer': 0 if pattern_future_trend['change'] > 0 else 1
    }


def random_question_type(pattern):
    rd = np.random.uniform()
    if rd < 0.5:
        return identify_question(pattern, 3)
    else:
        return predict_question(pattern)


def choose_pattern_leitner(user):
    # BOXES: 1, 2, 3, 4, 5
    BOX_PROBABILITIES = [0.3, 0.2, 0.2, 0.15, 0.15]
    
    user_boxes = LeitnerBox.objects.filter(user=user)
    user_max_box_reached = user_boxes.aggregate(Max('box_number'))['box_number__max']

    modified_probabilies = BOX_PROBABILITIES[:user_max_box_reached+1]
    normal_modified_probabilities = [p / sum(modified_probabilies) for p in modified_probabilies]
    box = np.random.choice(user_max_box_reached+1, 1, p=normal_modified_probabilities)[0]
    
    patterns = list(user_boxes.filter(box_number=box))
    selected_pattern = np.random.choice(patterns, 1)[0]
    
    return selected_pattern