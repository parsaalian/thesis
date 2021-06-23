from django.db import models
from dateutil.relativedelta import relativedelta


class Stock(models.Model):
    BOURSE = 'bourse'
    FARA_BOURSE = 'fara_bourse'
    PAYEH_FARA_BOURSE = 'payeh_fara_bourse'
    STOCK_MARKET_TYPES = (
        (BOURSE, 'بورس'),
        (FARA_BOURSE, 'فرابورس'),
        (PAYEH_FARA_BOURSE, 'پایه فرابورس'),
    )

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=500)
    CIsin = models.CharField(max_length=20)
    stock_market_type = models.CharField(
        max_length=20,
        choices=STOCK_MARKET_TYPES,
        default='',
    )
    category = models.CharField(max_length=100)
    stock_type_number = models.IntegerField(default=0)
    base_volume = models.IntegerField(default=0)
    num_stocks = models.BigIntegerField(default=0)
    par_value = models.IntegerField(default=0)
    valid = models.BooleanField(default=True)
    new_stock_id = models.BigIntegerField(blank=True, null=True)

    @property
    def detail_url(self):
        return 'http://www.tsetmc.com/Loader.aspx?ParTree=15131J&i={}'.format(self.id)

    @staticmethod
    def get_stock_market_type(flow):
        if flow == 1:
            return Stock.BOURSE
        if flow == 2:
            return Stock.FARA_BOURSE
        if flow == 4:
            return Stock.PAYEH_FARA_BOURSE

    @staticmethod
    def get_preemption_rights():
        return Stock.objects.filter(stock_type_number__in=[400, 403, 404])

    @staticmethod
    def get_housing_preemption_rights():
        return Stock.objects.filter(category='اوراق حق تقدم استفاده از تسهیلات مسکن')

    @staticmethod
    def get_traded_stocks(only_id):
        traded_stock_ids = list(StockHistory.objects.values_list('stock_id', flat=True).distinct())
        traded_stocks = Stock.objects.filter(id__in=traded_stock_ids)
        if only_id:
            traded_stocks = list(traded_stocks.values_list('id', flat=True))
        return traded_stocks


class StockHistoryBase(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    date = models.DateField(db_index=True)
    max_price = models.IntegerField()
    min_price = models.IntegerField()
    last_price = models.IntegerField()
    last_deal_price = models.IntegerField()
    first_price = models.IntegerField()
    yesterday_price = models.IntegerField()
    value = models.BigIntegerField()
    volume = models.BigIntegerField()
    count = models.IntegerField()

    class Meta:
        abstract = True


class StockHistory(StockHistoryBase):
    class Meta:
        unique_together = ('stock', 'date',)

    @staticmethod
    def load_stock_near_date(date, stock_id, from_date=None):
        start_date = (date + relativedelta(months=-1)) if from_date is None else from_date
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = date.strftime('%Y-%m-%d')

        sql_query = '''
            select *
            from bourse_refs_api_stockhistory
            where (stock_id, date) in (
            	select stock_id, max(date) from bourse_refs_api_stockhistory
            	where stock_id=%s and %s<=date and date<=%s
            	group by stock_id
            )
        '''

        return StockHistory.objects.raw(sql_query, [stock_id, start_date, end_date])[0]

    @staticmethod
    def load_near_date(date):
        start_date = (date + relativedelta(months=-1)).strftime('%Y-%m-%d')
        end_date = date.strftime('%Y-%m-%d')

        sql_query = '''
            select *
            from bourse_refs_api_stockhistory
            where (stock_id, date) in (
                select stock_id, max(date) from bourse_refs_api_stockhistory
                where %s<=date and date<=%s
                group by stock_id
            )
        '''

        stock_history = {}
        for sh in StockHistory.objects.raw(sql_query, [start_date, end_date]):
            stock_history[sh.stock_id] = sh

        return stock_history

    @staticmethod
    def load_last_open_date_price(date):
        sql_query = '''
            select id, stock_id, last_price
            from bourse_refs_api_stockhistory
            where (stock_id, date) in (
                select stock_id, max(date) from bourse_refs_api_stockhistory
                where date<=%s
                group by stock_id
            )
        '''

        stock_history = {}
        for sh in StockHistory.objects.raw(sql_query, [date.strftime('%Y-%m-%d')]):
            stock_history[sh.stock_id] = sh.last_price

        return stock_history


class StockHistoryOnline(StockHistoryBase):
    time = models.DateTimeField(db_index=True)

    class Meta:
        unique_together = ('stock', 'date', 'time')


class StockInfo(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    datetime = models.DateTimeField()
    date = models.DateField(db_index=True)
    last_trade_price = models.PositiveIntegerField()
    last_price = models.PositiveIntegerField()
    first_price = models.PositiveIntegerField()
    yesterday_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    min_price = models.PositiveIntegerField()
    trade_count = models.PositiveIntegerField()
    trade_volume = models.BigIntegerField()
    trade_value = models.BigIntegerField()


class BuyAndSellOrderBase(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    datetime = models.DateTimeField()
    date = models.DateField(db_index=True)
    position = models.IntegerField()
    buy_count = models.IntegerField()
    buy_volume = models.BigIntegerField()
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    sell_volume = models.BigIntegerField()
    sell_count = models.IntegerField()

    class Meta:
        abstract = True


class BuyAndSellOrder(BuyAndSellOrderBase):
    pass


class BuyAndSellOrderOnline(BuyAndSellOrderBase):
    class Meta:
        unique_together = ('stock', 'position',)


class NaturalLegalPersonsTrade(models.Model):
    SELL = 'sell'
    BUY = 'buy'
    TRADE_TYPES = (
        (SELL, 'sell'),
        (BUY, 'buy'),
    )
    NATURAL_PERSON = 'natural'
    LEGAL_PERSON = 'legal'
    PERSON_TYPES = (
        (NATURAL_PERSON, 'natural person'),
        (LEGAL_PERSON, 'legal person'),
    )
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    date = models.DateField(db_index=True)
    type = models.CharField(max_length=10, choices=TRADE_TYPES)
    person_type = models.CharField(max_length=10, choices=PERSON_TYPES)

    count = models.IntegerField()
    volume = models.BigIntegerField()
    value = models.BigIntegerField()
    average_price = models.FloatField()

    class Meta:
        index_together = [
            ('stock', 'date'),
        ]


class NaturalLegalPersonsTradeOnline(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    date = models.DateField(db_index=True)
    datetime = models.DateTimeField()
    buy_count_legal = models.IntegerField()
    buy_count_natural = models.IntegerField()
    buy_volume_legal = models.BigIntegerField()
    buy_volume_natural = models.BigIntegerField()
    sell_count_legal = models.IntegerField()
    sell_count_natural = models.IntegerField()
    sell_volume_legal = models.BigIntegerField()
    sell_volume_natural = models.BigIntegerField()


class MarketIndex(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    stocks = models.ManyToManyField(Stock)


class MarketIndexHistory(models.Model):
    market_index = models.ForeignKey(MarketIndex, on_delete=models.PROTECT)
    date = models.DateField(db_index=True)

    close_value = models.IntegerField() # XNivInuClMresIbs
    open_value = models.IntegerField() # XNivInuPrDifMresIbs
    high_value = models.IntegerField() # XNivInuPhMresIbs
    low_value = models.IntegerField() # XNivInuPbMresIbs

    yesterday_market_cap = models.FloatField() # QCapBsRfVIbs
    adjustment_coefficient = models.FloatField() # KAjCapBzIbs

    class Meta:
        unique_together = ('market_index', 'date',)


class CapitalIncrease(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    date = models.DateField()
    number_of_new_shares = models.BigIntegerField()
    number_of_old_shares = models.BigIntegerField()

    class Meta:
        unique_together = ('stock', 'date')