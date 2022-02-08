from .models import HistoricalMarketData


class HistoricalDataRow:
    def __init__(self, data: HistoricalMarketData, ma_20: float, ma_50: float):
        # print(ma_50)
        self.data = data
        self.ma_20 = ma_20
        self.ma_50 = ma_50
