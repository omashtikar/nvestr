from django.db import models


class Company(models.Model):
    symbol = models.CharField(max_length=20)
    # Creates a unique stock ID for each stock.
    company_name = models.CharField(max_length=200)
    # Name of the company relating to the stock ID.

    class Meta:
        constraints = [models.UniqueConstraint(fields=['symbol'], name="unique_symbol")]

    def __str__(self):
        return self.symbol


class CurrentMarketData(models.Model):
    stock = models.ForeignKey(Company, on_delete=models.CASCADE)
    # Foreign key of the stock name.
    price = models.FloatField()
    # Current price of the stock.
    updated_at = models.DateTimeField("Last updated at")
    # Time of last update of the current market data.

    class Meta:
        constraints = [models.UniqueConstraint(fields=['stock'], name="unique_stock")]

    def __str__(self):
        return str(self.stock) + " " + str(self.price) + " " + str(self.updated_at)


class HistoricalMarketData(models.Model):
    stock = models.ForeignKey(Company, on_delete=models.CASCADE)
    open = models.FloatField()
    # opening price when the stock market opens for the stock.
    close = models.FloatField()
    # closing price when the stock market closes for the stock.
    high = models.FloatField()
    # highest recorded price of the stock recorded when the market was open.
    low = models.FloatField()
    # lowest dip in the price of the stock when the market was open.
    volume = models.IntegerField()
    # number of stocks being traded at the current time
    trading_date = models.DateField()
    # date at which a trade of the stock is being made.

    class Meta:
        constraints = [models.UniqueConstraint(fields=['stock', 'trading_date'], name="unique_stock_and_trading_date")]

    def __str__(self):
        return str(self.stock) + " " + str(self.close) + " " + str(self.trading_date)



