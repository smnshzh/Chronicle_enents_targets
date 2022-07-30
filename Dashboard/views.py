from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from .models import data
import pandas as pd
def dashboard(request):
    datas = data.objects.all().order_by("date")
    df_sale = pd.read_excel(datas[0].sale.path)
    df_return = pd.read_excel(datas[0].returnSale.path)
    name = datas[0].name
    context = {"sale":df_sale,
               "retuen":df_return,
               "name":name}

    return render(request,'Dash1.html',context)

def flex(request):


    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = pd.read_json('json.json')
    data = dataset
    print(data)
    return JsonResponse(data, safe=False)
