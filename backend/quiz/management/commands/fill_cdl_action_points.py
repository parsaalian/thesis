import numpy as np
import pandas as pd
import pandas_ta as ta
from ta.utils import dropna
from tqdm import tqdm as tqdm
from django.core.management.base import BaseCommand
from quiz.models import Pattern, HistoricalPatternActionPoint
from bourse_refs_api.models import Stock, StockHistory



class Command(BaseCommand):
    help = 'Fills Pattern & PatternArticle tables from crawled data'
    
    
    def handle(self, *args, **kwargs):
        print('downloading stock history data...')
        queryset = list(StockHistory.objects.all().values())
        df = pd.DataFrame(queryset)
        df.stock_id = list(map(lambda x: str(x['stock_id']), queryset))
        df = df.sort_values('date').reset_index(drop=True)
        df = dropna(df)
        df = df.sort_values(['stock_id', 'date'])
        df = df.rename(columns={
            'max_price': 'high',
            'min_price': 'low',
            'last_deal_price': 'close',
            'first_price': 'open'
        })
        
        def add_cdl_patterns(group):
            try:
                return pd.concat([group, group.ta.cdl_pattern()], axis=1)
            except:
                return pd.DataFrame()

        print('adding candle patterns...')
        df = df.groupby('stock_id').apply(add_cdl_patterns)
        df = df.rename(columns={ 'CDL_DOJI_10_0.1': 'CDL_DOJI' })
        
        print('inserting patterns into databse...')
        patterns = Pattern.objects.all()
        for pattern in tqdm(patterns):
            df_pattern_key = 'CDL_' + pattern.pattern_key.upper()
            sub_df = df[df[df_pattern_key] != 0].drop(['stock_id'], axis=1).reset_index()[[
                'stock_id', 'date', df_pattern_key
            ]]
            entries = list(map(
                lambda row: HistoricalPatternActionPoint(
                    stock_id=int(row[0]),
                    pattern=pattern,
                    date=row[1],
                    value=row[2]
                ),
                list(sub_df.values)
            ))
            HistoricalPatternActionPoint.objects.bulk_create(entries, ignore_conflicts=True)
        
        print(len(HistoricalPatternActionPoint.objects.all()))
