import pandas as pd
from dateutil.relativedelta import relativedelta
from tqdm import tqdm as tqdm
from django.core.management.base import BaseCommand

from quiz.utils import trend
from quiz.models import Pattern, HistoricalPatternActionPoint, PatternStatistics
from bourse_refs_api.models import StockHistory


class Command(BaseCommand):
    help = 'Compute and fills statistics for each pattern'
    
    
    def add_arguments(self, parser):
        parser.add_argument('--ma', type=int, help='period of moving average', default=14)
        parser.add_argument('--before', type=int, help='span of before date', default=14)
        parser.add_argument('--after', type=int, help='span of after date', default=60)
        parser.add_argument('--max_count', type=int, help='maximum number of samples', default=1000)
    
    
    def handle(self, *args, **kwargs):
        print('downloading stock history data...')
        queryset = list(StockHistory.objects.all().values())
        history_df = pd.DataFrame(queryset)
        history_df.stock_id = list(map(lambda x: str(x['stock_id']), queryset))
        history_df = history_df.sort_values(['stock_id', 'date'])
        history_df = history_df.rename(columns={
            'max_price': 'high',
            'min_price': 'low',
            'last_deal_price': 'close',
            'first_price': 'open',
        })
        
        patterns = list(Pattern.objects.all())
        
        print('calculating statistics...')
        
        for pattern in tqdm(patterns):
            queryset = list(HistoricalPatternActionPoint.objects.filter(pattern_id=pattern.pattern_key).values())
            pattern_df = pd.DataFrame(queryset)
            pattern_df.stock_id = list(map(lambda x: str(x['stock_id']), queryset))
            
            for value, group in pattern_df.groupby('value'):
                performance_list = []
                count = 0
                # shuffle for random selection of max_count rows
                if len(group) > kwargs.get('max_count'):
                    shuffled = group.sample(frac=1).reset_index(drop=True)
                else:
                    shuffled = group
                
                t = tqdm(total=min(kwargs.get('max_count'), len(shuffled)))
                
                for _, pivot in shuffled.iterrows():
                    t.update()
                    history = history_df[
                        (history_df.stock_id == pivot.stock_id) &
                        (history_df.date >= pivot.date - relativedelta(days=kwargs.get('before'))) &
                        (history_df.date <= pivot.date + relativedelta(days=kwargs.get('after')))
                    ].set_index('date').sort_index()
                    performance_list.append(trend(history, pivot, kwargs.get('ma')))
                    count += 1
                    if count == kwargs.get('max_count'):
                        break;
                t.close()
                
                perdf = pd.DataFrame(performance_list)
                perdf = perdf[(perdf.change != 0) & (perdf.time > 0)]
                stats = perdf.describe()
                try:
                    PatternStatistics.objects.update_or_create(
                        pattern=pattern,
                        value=value,
                        count=len(perdf),
                        change_mean=stats.loc['mean', 'change'],
                        change_std=stats.loc['std', 'change'],
                        change_min=stats.loc['min', 'change'],
                        change_25=stats.loc['25%', 'change'],
                        change_50=stats.loc['50%', 'change'],
                        change_75=stats.loc['75%', 'change'],
                        change_max=stats.loc['max', 'change'],
                        time_mean=int(stats.loc['mean', 'time']),
                        time_std=int(stats.loc['std', 'time']),
                        time_min=int(stats.loc['min', 'time']),
                        time_25=int(stats.loc['25%', 'time']),
                        time_50=int(stats.loc['50%', 'time']),
                        time_75=int(stats.loc['75%', 'time']),
                        time_max=int(stats.loc['max', 'time']),
                        positive_rate=len(perdf[perdf.change > 0]) / len(perdf)
                    )
                except:
                    pass
