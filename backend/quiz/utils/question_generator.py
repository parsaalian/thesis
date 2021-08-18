import numpy as np
import pandas as pd
from random import choice
from dateutil.relativedelta import relativedelta
from django.db.models import Max

from bourse_refs_api.models import StockHistory
from .trend import trend
from ..models import Pattern, HistoricalPatternActionPoint, LeitnerBox


def get_random_action_point(pattern):
    action_point = choice(HistoricalPatternActionPoint.objects.filter(pattern=pattern))
    return action_point


def identify_question(pattern, wrong_choices_count):
    patterns = list(map(lambda x: x.pattern_key, Pattern.objects.all()))
    patterns = list(filter(lambda x: x != pattern.pattern_key, patterns))
    other_choices = np.random.choice(patterns, wrong_choices_count, replace=False)
    all_choices = [pattern.pattern_key, *other_choices]
    np.random.shuffle(all_choices)
    print(all_choices)
    return {
        'prompt': 'Which pattern is seen at the end of the chart?',
        'choices': all_choices,
        'answer': all_choices.index(pattern.pattern_key)
    }


def predict_question(pattern, history):
    history_df = pd.DataFrame(list(history.values())).set_index('date').sort_index().rename(columns={
        'max_price': 'high',
        'min_price': 'low',
        'last_deal_price': 'close',
        'first_price': 'open',
    })
    
    pattern_future_trend = trend(history_df, pattern, ma=14)
    return {
        'prompt': 'What will be the trend after this point?',
        'choices': ['Bullish', 'Bearish'],
        'answer': 0 if pattern_future_trend['change'] > 0 else 1
    }


def random_question_type(action_point, history):
    rd = np.random.uniform()
    if rd < 0.5:
        return identify_question(action_point.pattern, 3)
    else:
        return predict_question(action_point, history)


def choose_pattern_leitner(user):
    # BOXES: 1, 2, 3, 4, 5
    BOX_PROBABILITIES = [0.3, 0.2, 0.2, 0.15, 0.15]
    
    user_boxes = LeitnerBox.objects.filter(user=user)
        
    user_max_box_reached = user_boxes.aggregate(Max('box_number'))['box_number__max']

    modified_probabilies = BOX_PROBABILITIES[:user_max_box_reached+1]
    normal_modified_probabilities = [p / sum(modified_probabilies) for p in modified_probabilies]
    box = np.random.choice(user_max_box_reached+1, 1, p=normal_modified_probabilities)[0]
    
    patterns = list(user_boxes.filter(box_number=box))
    selected_pattern = np.random.choice(patterns, 1)[0].pattern
    
    return selected_pattern