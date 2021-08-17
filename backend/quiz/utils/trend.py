import pandas as pd
import pandas_ta as ta
from dateutil.relativedelta import relativedelta


def trend(history, pivot, ma=14):
    if len(history) < ma:
        return { 'change': 0, 'time': 0 }
    
    sma = ta.sma(history.close, length=ma).dropna()
    
    suprimums = pd.concat([
        sma[(sma.shift(1) < sma) & (sma.shift(-1) < sma)],
        sma[(sma.shift(1) > sma) & (sma.shift(-1) > sma)]]
    )
    
    if len(suprimums) > 0:
        suprimum_date = suprimums.index[0] - relativedelta(days=ma//2)
    else:
        suprimum_date = history.index[-1] - relativedelta(days=ma//2)
    
    try:
        suprimum_entry = history.loc[suprimum_date]
    except:
        suprimum_entry = history.loc[history.index[history.index.searchsorted(suprimum_date)]]
        
    return {
        'change': (suprimum_entry.close / history.loc[pivot.date, 'close'] - 1) * 100,
        'time': (suprimum_date - pivot.date).days
    }