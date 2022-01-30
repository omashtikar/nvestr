from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, 'nvestr/home_page.html', context)
