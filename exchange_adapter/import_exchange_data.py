import os, django, sys
# The two lines below allow us to use django models in this program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE","nvestr.settings")
django.setup()
get_symbol = input("Tell me the symbol: ")
import yfinance as yf
from market.models import Company, HistoricalMarketData

yf_ticker = yf.Ticker(get_symbol)
print(yf_ticker.info['longName'])
update_or_create_response = Company.objects.update_or_create({'company_name': yf_ticker.info['longName']}, symbol = get_symbol)
django_models_company = update_or_create_response[0]

hist = yf_ticker.history(period="max")
