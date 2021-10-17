from django.db import models


class Company(models.Model):
    symbol = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.symbol


class CurrentMarketData(models.Model):
    stock = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.FloatField()
    updated_at = models.DateTimeField("Last updated at")

    def __str__(self):
        return str(self.stock) + " " + str(self.price) + " " + str(self.updated_at)


class HistoricalMarketData(models.Model):
    stock = models.ForeignKey(Company, on_delete=models.CASCADE)
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.IntegerField()
    trading_date = models.DateField()

    def __str__(self):
        return str(self.stock) + " " + str(self.close) + " " + str(self.trading_date)
    