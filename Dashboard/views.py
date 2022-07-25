from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
import pandas as pd
def dashboard(request):


    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = pd.read_json('json.json')
    data = dataset
    print(data)
    return JsonResponse(data, safe=False)
