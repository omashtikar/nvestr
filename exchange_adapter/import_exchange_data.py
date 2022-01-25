import os, django, sys
# The two lines below allow us to use django models in this program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE","nvestr.settings")
django.setup()
get_symbol = input("Tell me the symbol: ")
import yfinance as yf
from market.models import Company, HistoricalMarketData
from django.utils import timezone

yf_ticker = yf.Ticker(get_symbol)
print(yf_ticker.info['longName'])
update_or_create_response = Company.objects.update_or_create({'company_name': yf_ticker.info['longName']}, symbol = get_symbol)
django_models_company = update_or_create_response[0]

hist = yf_ticker.history(period="max").to_dict('index')

for trade_date_from_hist in hist:
    HistoricalMarketData.objects.update_or_create({'open': hist[trade_date_from_hist]['Open'],
                                                   'high': hist[trade_date_from_hist]['High'],
                                                   'low': hist[trade_date_from_hist]['Low'],
                                                   'close': hist[trade_date_from_hist]['Close'],
                                                   'volume': hist[trade_date_from_hist]['Volume']
                                                   }, stock=django_models_company, trading_date=trade_date_from_hist)
    print('Imported {} record'.format(trade_date_from_hist.to_pydatetime()))
