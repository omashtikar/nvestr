from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.index, name='company_list'),
    path('<int:company_id>', views.company_data, name='company_data')
]
