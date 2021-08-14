import json
from markdownify import markdownify
from django.core.management.base import BaseCommand
from quiz.models import Pattern, PatternArticle


pattern_names_mapping = {
    'two crows': '2crows',
    'three black crows': '3blackcrows',
    'three inside': '3inside',
    'three line strike': '3linestrike',
    'three outside': '3outside',
    'three stars in south': '3starsinsouth',
    'three white soldiers': '3whitesoldiers',
    'abandoned baby': 'abandonedbaby',
    'advance block': 'advanceblock',
    'belt hold': 'belthold',
    'break away': 'breakaway',
    'closing marubozu': 'closingmarubozu',
    'conceal babyswall': 'concealbabyswall',
    'counterattack': 'counterattack',
    'dark cloud cover': 'darkcloudcover',
    'doji': 'doji',
    'doji star': 'dojistar',
    'dragonfly doji': 'dragonflydoji',
    'engulfing': 'engulfing',
    'evening doji star': 'eveningdojistar',
    'evening star': 'eveningstar',
    'gap side side white': 'gapsidesidewhite',
    'gravestone doji': 'gravestonedoji',
    'hammer': 'hammer',
    'hanging man': 'hangingman',
    'harami': 'harami',
    'harami cross': 'haramicross',
    'high wave': 'highwave',
    'hikkake': 'hikkake',
    'hikkake modified': 'hikkakemod',
    'identical three crows': 'identical3crows',
    'in neck': 'inneck',
    'inside': 'inside',
    'inverted hammer': 'invertedhammer',
    'kicking': 'kicking',
    'kicking by length': 'kickingbylength',
    'ladder bottom': 'ladderbottom',
    'long legged doji': 'longleggeddoji',
    'long line': 'longline',
    'marubozu': 'marubozu',
    'matching glow': 'matchinglow',
    'mat hold': 'mathold',
    'morning doji star': 'morningdojistar',
    'morning star': 'morningstar',
    'on neck': 'onneck',
    'piercing': 'piercing',
    'rickshaw man': 'rickshawman',
    'rising three methods': 'risefall3methods',
    'falling three methods': 'risefall3methods',
    'separating lines': 'separatinglines',
    'shooting star': 'shootingstar',
    'short line': 'shortline',
    'spinning top': 'spinningtop',
    'stalled pattern': 'stalledpattern',
    'stick sandwich': 'sticksandwich',
    'takuri': 'takuri',
    'tasuki gap': 'tasukigap',
    'thrusting': 'thrusting',
    'tri star': 'tristar',
    'unique three river': 'unique3river',
    'upside gap two crows': 'upsidegap2crows',
    'x side gap three methods': 'xsidegap3methods'
}


class Command(BaseCommand):
    help = 'Fills Pattern & PatternArticle tables from crawled data'
    
    
    def add_arguments(self, parser):
        parser.add_argument('--crawled_data', type=str, help='location of crawled data json')
    
    
    def handle(self, *args, **kwargs):
        pattern_data = {}
        with open(kwargs.get('crawled_data'), 'r') as f:
            pattern_data = json.load(f)
        
        for value in list(pattern_names_mapping.values()):
            pattern = Pattern(pattern_key=value)
            pattern.save()
        
        for key, value in pattern_names_mapping.items():
            if key in pattern_data:
                for article in pattern_data[key]:
                    pattern_article = PatternArticle(
                        pattern=Pattern.objects.get(pattern_key=value),
                        href=article['href'],
                        title=article['title'],
                        author=article['author'],
                        body=markdownify(article['body'].replace('\n', ''))
                    )
                    pattern_article.save()
