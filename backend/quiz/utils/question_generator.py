import numpy as np
from ..models import Pattern


def identify_question(pattern, wrong_choices_count):
    patterns = list(map(lambda x: x.pattern_key, Pattern.objects.all()))
    patterns = list(filter(lambda x: x != pattern, patterns))
    other_choices = np.random.choice(patterns, wrong_choices_count, replace=False)
    choices = np.random.permutation([pattern, *other_choices]),
    return {
        'prompt': 'Which pattern is seen at the end of the chart?',
        'choices': choices,
        'answer': choices.index(pattern)
    }


def predict_question():
    pass
