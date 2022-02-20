from .models import HistoricalMarketData
from enum import IntEnum

class Trend(IntEnum):
    UNKNOWN = 0
    UP = 1
    DOWN = 2


class HistoricalDataRow:
    def __init__(self, data: HistoricalMarketData, ma_20: float, ma_50: float):
        # print(ma_50)
        self.data = data
        self.ma_20 = ma_20
        self.ma_50 = ma_50
        self.trend_reversed = False
        self.trend = Trend.UNKNOWN
        self.signal = 'IGNORE'


def set_trend(rows: list) -> list:
    prev_trend = Trend.UNKNOWN
    ret = []
    for r in rows[::-1]:
        if r.ma_20 and r.ma_50:
            if r.ma_20 > r.ma_50:
                r.trend = Trend.UP
            if r.ma_50 > r.ma_20:
                r.trend = Trend.DOWN
            if prev_trend != r.trend:
                r.trend_reversed = True
            prev_trend = r.trend
            if r.trend == Trend.UP and r.trend_reversed:
                r.signal = 'BUY'
            if r.trend == Trend.UP and not r.trend_reversed:
                r.signal = 'HOLD / IGNORE'
            if r.trend == Trend.DOWN and r.trend_reversed:
                r.signal = 'SELL'
            if r.trend == Trend.DOWN and not r.trend_reversed:
                r.signal = 'SELL / IGNORE'
        ret.append(r)
    return list(reversed(ret))

