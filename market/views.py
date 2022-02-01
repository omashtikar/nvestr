from django.http import HttpResponse
from django.shortcuts import render
from .models import Company


def index(request):
    company_list = list(Company.objects.all())
    context = {'company_list': company_list}
    return render(request, 'market/company_list.html', context)

