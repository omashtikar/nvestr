from django.http import HttpResponse
from django.shortcuts import render
from .models import Company, HistoricalMarketData
from .moving_average import moving_average
from .model_extensions import HistoricalDataRow

def index(request):
    company_list = list(Company.objects.all())
    context = {'company_list': company_list}
    return render(request, 'market/company_list.html', context)


def company_data(request, company_id):
    company_obj = Company.objects.get(pk=company_id)
    historical_data = list(HistoricalMarketData.objects.filter(stock=company_obj).order_by('-trading_date'))
    close_price_list = []
    for h in historical_data:
        close_price_list.append(h.close)
    ma_20_list = moving_average(close_price_list, 20)
    ma_50_list = moving_average(close_price_list, 50)
    len_ma_20 = len(ma_20_list)
    len_ma_50 = len(ma_50_list)

    # print(ma_50_list)

    rows = []
    counter = 0
    for h in historical_data:
        ma_20 = None
        if counter < len_ma_20:
            ma_20 = ma_20_list[counter]
        ma_50 = None
        if counter < len_ma_50:
            ma_50 = ma_50_list[counter]
        rows.append(HistoricalDataRow(h, ma_20, ma_50))
        counter += 1

    context = {'historical_data_list': rows, 'company': company_obj}
    return render(request, 'market/historical_data.html', context)

